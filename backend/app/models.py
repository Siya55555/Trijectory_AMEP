from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    role = Column(String)  # student, teacher, admin
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    assessments = relationship("Assessment", back_populates="student")
    engagement_records = relationship("EngagementRecord", back_populates="student")
    mastery_profiles = relationship("MasteryProfile", back_populates="student")

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    teacher_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Assessment(Base):
    __tablename__ = "assessments"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    score = Column(Float)
    concepts = Column(JSON)  # {"concept1": score, "concept2": score, ...}
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    student = relationship("User", back_populates="assessments")

class MasteryProfile(Base):
    __tablename__ = "mastery_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    concept = Column(String, index=True)
    mastery_score = Column(Float, default=0.0)  # 0-100
    attempt_count = Column(Integer, default=0)
    correct_count = Column(Integer, default=0)
    last_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    student = relationship("User", back_populates="mastery_profiles")

class EngagementRecord(Base):
    __tablename__ = "engagement_records"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    poll_response = Column(JSON)  # Anonymous poll responses
    confusion_index = Column(Float, default=0.0)  # 0-100, from camera detection
    participation_type = Column(String)  # explicit, implicit
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    student = relationship("User", back_populates="engagement_records")

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String, index=True)
    description = Column(Text)
    template = Column(JSON)  # Project template data
    status = Column(String)  # active, completed, archived
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class PBLTeam(Base):
    __tablename__ = "pbl_teams"
    
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    name = Column(String)
    members = Column(JSON)  # [{user_id, role}, ...]
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class HomeworkAssignment(Base):
    __tablename__ = "homework_assignments"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    concept = Column(String)
    difficulty_level = Column(Integer)  # 1-5, based on ZPD
    assigned_at = Column(DateTime(timezone=True), server_default=func.now())
    completed = Column(Boolean, default=False)
    score = Column(Float, nullable=True)
