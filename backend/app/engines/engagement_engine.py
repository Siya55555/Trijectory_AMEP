"""
Engagement Engine - Tracks real-time student engagement
Combines explicit (polls) and implicit (confusion detection) metrics
"""

from app import models
from sqlalchemy.orm import Session
from typing import Dict, List

class EngagementEngine:
    def __init__(self):
        self.confusion_weight = 0.4  # Weight for confusion index
        self.participation_weight = 0.6  # Weight for explicit participation
    
    def calculate_engagement_index(
        self,
        student_id: int,
        course_id: int,
        db: Session
    ) -> float:
        """
        Calculate comprehensive engagement index (0-100) for a student
        
        Args:
            student_id: Student identifier
            course_id: Course identifier
            db: Database session
            
        Returns:
            Engagement index (0-100)
        """
        
        records = db.query(models.EngagementRecord).filter(
            models.EngagementRecord.student_id == student_id,
            models.EngagementRecord.course_id == course_id
        ).all()
        
        if not records:
            return 0.0
        
        # Calculate participation score
        participation_score = min(100, len(records) * 4)  # 25 interactions = 100
        
        # Calculate confusion management (lower confusion = higher score)
        avg_confusion = sum([r.confusion_index for r in records]) / len(records)
        confusion_score = 100 - avg_confusion  # Inverse relationship
        
        # Weighted average
        engagement_index = (
            participation_score * self.participation_weight +
            confusion_score * self.confusion_weight
        )
        
        return engagement_index
    
    def get_class_engagement_summary(
        self,
        course_id: int,
        db: Session
    ) -> Dict:
        """
        Get aggregated engagement metrics for entire class
        
        Args:
            course_id: Course identifier
            db: Database session
            
        Returns:
            Dictionary with class-wide metrics
        """
        
        records = db.query(models.EngagementRecord).filter(
            models.EngagementRecord.course_id == course_id
        ).all()
        
        if not records:
            return {
                "course_id": course_id,
                "total_students_engaged": 0,
                "avg_engagement_index": 0.0,
                "avg_confusion_index": 0.0,
                "participation_rate": 0.0
            }
        
        unique_students = len(set(r.student_id for r in records))
        avg_confusion = sum([r.confusion_index for r in records]) / len(records)
        
        return {
            "course_id": course_id,
            "total_students_engaged": unique_students,
            "avg_engagement_index": sum([r.confusion_index for r in records]) / len(records),
            "avg_confusion_index": avg_confusion,
            "participation_rate": (unique_students / 25) * 100  # Assuming 25 students
        }
    
    def identify_disengaged_students(
        self,
        course_id: int,
        db: Session,
        threshold: float = 40.0
    ) -> List[int]:
        """
        Identify students with low engagement (potential risk)
        
        Args:
            course_id: Course identifier
            db: Database session
            threshold: Engagement score threshold (0-100)
            
        Returns:
            List of student IDs with low engagement
        """
        
        all_students = db.query(models.User).filter(
            models.User.role == "student"
        ).all()
        
        disengaged = []
        for student in all_students:
            index = self.calculate_engagement_index(
                student.id,
                course_id,
                db
            )
            if index < threshold:
                disengaged.append(student.id)
        
        return disengaged
