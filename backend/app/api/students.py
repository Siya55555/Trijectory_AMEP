from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class StudentProfile(BaseModel):
    id: int
    email: str
    name: str
    role: str

    class Config:
        from_attributes = True

@router.get("/profile/{student_id}", response_model=StudentProfile)
async def get_student_profile(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.User).filter(models.User.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/{student_id}/mastery")
async def get_student_mastery(student_id: int, db: Session = Depends(get_db)):
    """Get student's concept mastery profile"""
    mastery_data = db.query(models.MasteryProfile).filter(
        models.MasteryProfile.student_id == student_id
    ).all()
    
    return {
        "student_id": student_id,
        "mastery_profiles": [
            {
                "concept": m.concept,
                "mastery_score": m.mastery_score,
                "attempt_count": m.attempt_count,
                "correct_count": m.correct_count
            }
            for m in mastery_data
        ]
    }

@router.get("/{student_id}/assignments")
async def get_student_assignments(student_id: int, db: Session = Depends(get_db)):
    """Get adaptive homework assignments"""
    assignments = db.query(models.HomeworkAssignment).filter(
        models.HomeworkAssignment.student_id == student_id
    ).all()
    
    return {
        "assignments": [
            {
                "id": a.id,
                "concept": a.concept,
                "difficulty_level": a.difficulty_level,
                "completed": a.completed,
                "score": a.score
            }
            for a in assignments
        ]
    }

@router.post("/{student_id}/projects/join")
async def join_project(student_id: int, project_id: int, db: Session = Depends(get_db)):
    """Student joins a PBL project"""
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return {"message": f"Student {student_id} joined project {project_id}"}
