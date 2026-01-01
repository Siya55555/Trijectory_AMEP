from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from pydantic import BaseModel

router = APIRouter()

class AssessmentSubmission(BaseModel):
    student_id: int
    course_id: int
    concepts: dict
    score: float

@router.post("/submit")
async def submit_assessment(assessment: AssessmentSubmission, db: Session = Depends(get_db)):
    """Submit assessment results"""
    
    new_assessment = models.Assessment(
        student_id=assessment.student_id,
        course_id=assessment.course_id,
        score=assessment.score,
        concepts=assessment.concepts
    )
    db.add(new_assessment)
    db.commit()
    db.refresh(new_assessment)
    
    return {
        "assessment_id": new_assessment.id,
        "message": "Assessment submitted successfully"
    }

@router.get("/{assessment_id}")
async def get_assessment(assessment_id: int, db: Session = Depends(get_db)):
    """Get assessment details"""
    assessment = db.query(models.Assessment).filter(
        models.Assessment.id == assessment_id
    ).first()
    
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    
    return assessment
