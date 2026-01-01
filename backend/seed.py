"""
Seed data for testing AMEP Platform
"""

from app.database import SessionLocal
from app import models
from datetime import datetime

def seed_database():
    """Populate database with sample data"""
    db = SessionLocal()
    
    try:
        # Clear existing data
        db.query(models.User).delete()
        db.query(models.Course).delete()
        db.commit()
        
        # Create users
        teacher = models.User(
            email="teacher@example.com",
            name="Ms. Sarah Johnson",
            role="teacher"
        )
        admin = models.User(
            email="admin@example.com",
            name="Admin User",
            role="admin"
        )
        
        db.add(teacher)
        db.add(admin)
        db.commit()
        
        # Create students
        students = []
        for i in range(1, 6):
            student = models.User(
                email=f"student{i}@example.com",
                name=f"Student {i}",
                role="student"
            )
            students.append(student)
            db.add(student)
        
        db.commit()
        
        # Create course
        course = models.Course(
            name="Advanced Mathematics",
            description="Comprehensive mathematics course covering algebra, geometry, and calculus",
            teacher_id=teacher.id
        )
        db.add(course)
        db.commit()
        
        # Create mastery profiles
        concepts = ["Algebra", "Geometry", "Calculus", "Trigonometry"]
        for student in students:
            for concept in concepts:
                mastery = models.MasteryProfile(
                    student_id=student.id,
                    concept=concept,
                    mastery_score=45 + (hash(f"{student.id}{concept}") % 40),
                    attempt_count=10,
                    correct_count=6
                )
                db.add(mastery)
        
        db.commit()
        
        # Create engagement records
        for student in students:
            engagement = models.EngagementRecord(
                student_id=student.id,
                course_id=course.id,
                poll_response={"question_1": "agree"},
                confusion_index=25.0,
                participation_type="explicit"
            )
            db.add(engagement)
        
        db.commit()
        
        # Create projects
        project = models.Project(
            course_id=course.id,
            title="Smart City Design",
            description="Design a sustainable smart city",
            template={"phase": 1},
            status="active"
        )
        db.add(project)
        db.commit()
        
        print("✓ Database seeded successfully!")
        
    except Exception as e:
        db.rollback()
        print(f"✗ Error seeding database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
