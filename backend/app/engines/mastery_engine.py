"""
Mastery Engine - Implements Knowledge Tracing
Updates student concept mastery based on assessment performance
"""

from app import models
from sqlalchemy.orm import Session

class MasteryEngine:
    def __init__(self, initial_p_correct: float = 0.5, learning_rate: float = 0.1):
        """
        Initialize Mastery Engine with Knowledge Tracing parameters
        
        Args:
            initial_p_correct: Initial probability of correct response
            learning_rate: How much mastery improves per correct attempt
        """
        self.initial_p_correct = initial_p_correct
        self.learning_rate = learning_rate
    
    def update_mastery_score(
        self,
        student_id: int,
        concept: str,
        correct: bool,
        difficulty: int,
        db: Session
    ) -> float:
        """
        Update mastery score using simplified Knowledge Tracing
        
        Args:
            student_id: Student identifier
            concept: Concept being assessed
            correct: Whether answer was correct
            difficulty: Problem difficulty (1-5)
            db: Database session
            
        Returns:
            Updated mastery score (0-100)
        """
        
        # Get or create mastery profile
        profile = db.query(models.MasteryProfile).filter(
            models.MasteryProfile.student_id == student_id,
            models.MasteryProfile.concept == concept
        ).first()
        
        if not profile:
            profile = models.MasteryProfile(
                student_id=student_id,
                concept=concept,
                mastery_score=0.0,
                attempt_count=0,
                correct_count=0
            )
            db.add(profile)
        
        # Update counts
        profile.attempt_count += 1
        if correct:
            profile.correct_count += 1
        
        # Calculate mastery score (0-100)
        # Weighted by difficulty: harder problems boost mastery more
        difficulty_weight = 1 + (difficulty - 1) * 0.1
        
        if correct:
            improvement = self.learning_rate * difficulty_weight * 10
            profile.mastery_score = min(100, profile.mastery_score + improvement)
        else:
            # Slight decrease on wrong answer
            profile.mastery_score = max(0, profile.mastery_score - 5)
        
        db.commit()
        db.refresh(profile)
        
        return float(profile.mastery_score)
    
    def get_mastery_profile(self, student_id: int, db: Session) -> dict:
        """Get overall mastery profile for a student"""
        profiles = db.query(models.MasteryProfile).filter(
            models.MasteryProfile.student_id == student_id
        ).all()
        
        return {
            "student_id": student_id,
            "concepts": [
                {
                    "concept": p.concept,
                    "mastery_score": p.mastery_score,
                    "attempts": p.attempt_count,
                    "correct": p.correct_count
                }
                for p in profiles
            ],
            "overall_mastery": sum([p.mastery_score for p in profiles]) / len(profiles) if profiles else 0
        }
