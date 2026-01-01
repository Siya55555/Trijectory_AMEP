from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from pydantic import BaseModel

router = APIRouter()

class EngagementData(BaseModel):
    student_id: int
    course_id: int
    poll_response: dict
    confusion_index: float
    participation_type: str

@router.post("/track")
async def track_engagement(data: EngagementData, db: Session = Depends(get_db)):
    """Track real-time student engagement (explicit & implicit)"""
    
    record = models.EngagementRecord(
        student_id=data.student_id,
        course_id=data.course_id,
        poll_response=data.poll_response,
        confusion_index=data.confusion_index,
        participation_type=data.participation_type
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    
    return {
        "record_id": record.id,
        "message": "Engagement tracked"
    }

@router.get("/class/{course_id}/summary")
async def get_class_engagement_summary(course_id: int, db: Session = Depends(get_db)):
    """Get aggregated class engagement metrics"""
    
    records = db.query(models.EngagementRecord).filter(
        models.EngagementRecord.course_id == course_id
    ).all()
    
    avg_confusion = sum([r.confusion_index for r in records]) / len(records) if records else 0
    participation_rate = (len(records) / 25) * 100 if records else 0
    
    return {
        "course_id": course_id,
        "total_responses": len(records),
        "avg_confusion_index": avg_confusion,
        "participation_rate": participation_rate
    }

@router.get("/{student_id}/history")
async def get_engagement_history(student_id: int, db: Session = Depends(get_db)):
    """Get student's engagement history"""
    
    history = db.query(models.EngagementRecord).filter(
        models.EngagementRecord.student_id == student_id
    ).all()
    
    return {
        "student_id": student_id,
        "engagement_records": len(history)
    }
