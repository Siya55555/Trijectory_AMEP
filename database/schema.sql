-- AMEP Database Schema

-- Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    role VARCHAR(50) CHECK (role IN ('student', 'teacher', 'admin')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Courses Table
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    teacher_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Assessments Table
CREATE TABLE assessments (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES users(id),
    course_id INTEGER REFERENCES courses(id),
    score FLOAT,
    concepts JSONB,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Mastery Profiles Table
CREATE TABLE mastery_profiles (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES users(id),
    concept VARCHAR(255),
    mastery_score FLOAT DEFAULT 0.0,
    attempt_count INTEGER DEFAULT 0,
    correct_count INTEGER DEFAULT 0,
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Engagement Records Table
CREATE TABLE engagement_records (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES users(id),
    course_id INTEGER REFERENCES courses(id),
    poll_response JSONB,
    confusion_index FLOAT DEFAULT 0.0,
    participation_type VARCHAR(50),
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Projects Table
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses(id),
    title VARCHAR(255),
    description TEXT,
    template JSONB,
    status VARCHAR(50) DEFAULT 'active',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- PBL Teams Table
CREATE TABLE pbl_teams (
    id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(id),
    name VARCHAR(255),
    members JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Homework Assignments Table
CREATE TABLE homework_assignments (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES users(id),
    concept VARCHAR(255),
    difficulty_level INTEGER CHECK (difficulty_level BETWEEN 1 AND 5),
    assigned_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed BOOLEAN DEFAULT FALSE,
    score FLOAT
);

-- Indexes for performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_assessments_student ON assessments(student_id);
CREATE INDEX idx_mastery_student_concept ON mastery_profiles(student_id, concept);
CREATE INDEX idx_engagement_student ON engagement_records(student_id);
CREATE INDEX idx_homework_student ON homework_assignments(student_id);
