from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from pydantic import BaseModel
from app.engines.mastery_engine import MasteryEngine

router = APIRouter()

class MasteryUpdate(BaseModel):
    student_id: int
    concept: str
    correct: bool
    difficulty: int

@router.post("/update")
async def update_mastery(data: MasteryUpdate, db: Session = Depends(get_db)):
    """Update student's concept mastery using Knowledge Tracing"""
    
    engine = MasteryEngine()
    new_score = engine.update_mastery_score(
        student_id=data.student_id,
        concept=data.concept,
        correct=data.correct,
        difficulty=data.difficulty,
        db=db
    )
    
    return {
        "student_id": data.student_id,
        "concept": data.concept,
        "new_mastery_score": new_score
    }

@router.get("/{student_id}/weak-concepts")
async def get_weak_concepts(student_id: int, db: Session = Depends(get_db)):
    """Identify weak concepts for adaptive learning"""
    
    mastery_data = db.query(models.MasteryProfile).filter(
        models.MasteryProfile.student_id == student_id
    ).all()
    
    weak_concepts = [m for m in mastery_data if m.mastery_score < 70]
    weak_concepts.sort(key=lambda x: x.mastery_score)
    
    return {
        "student_id": student_id,
        "weak_concepts": [
            {
                "concept": c.concept,
                "mastery_score": c.mastery_score,
                "zpd_level": max(1, min(5, int(c.mastery_score / 20) + 1))
            }
            for c in weak_concepts
        ]
    }

@router.post("/{student_id}/generate-homework")
async def generate_adaptive_homework(student_id: int, db: Session = Depends(get_db)):
    """Generate adaptive homework based on weak concepts (Zone of Proximal Development)"""
    
    weak_concepts = db.query(models.MasteryProfile).filter(
        models.MasteryProfile.student_id == student_id,
        models.MasteryProfile.mastery_score < 70
    ).all()
    
    assignments = []
    for concept in weak_concepts[:3]:  # Top 3 weak areas
        zpd_level = max(1, min(5, int(concept.mastery_score / 20) + 1))
        
        assignment = models.HomeworkAssignment(
            student_id=student_id,
            concept=concept.concept,
            difficulty_level=zpd_level
        )
        db.add(assignment)
        assignments.append({
            "concept": concept.concept,
            "difficulty_level": zpd_level
        })
    
    db.commit()
    
    return {
        "student_id": student_id,
        "generated_assignments": assignments
    }
