# Team: Trivengers
# Project: Trajectory (AMEP)
# Hackathon: Quasar 4.0

## Architecture Overview

AMEP is built with a modular, scalable architecture that separates concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                     USER INTERFACES                          │
│  Student Portal | Teacher Dashboard | Admin Portal          │
└────────────────────────┬────────────────────────────────────┘
                         │ (HTTP/REST)
┌────────────────────────▼────────────────────────────────────┐
│              FASTAPI BACKEND (APIs & Services)              │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
│  │  Engagement  │ │   Mastery    │ │ PBL Manager  │        │
│  │   Engine     │ │   Engine     │ │              │        │
│  └──────────────┘ └──────────────┘ └──────────────┘        │
│              ▲           ▲                ▲                  │
└──────────────┼───────────┼────────────────┼─────────────────┘
               │           │                │
┌──────────────▼───────────▼────────────────▼─────────────────┐
│           DATA & LOGIC LAYER (SQLAlchemy ORM)               │
│         ┌─────────────────────────────────────┐             │
│         │  Assessment | Homework | Tracking   │             │
│         └─────────────────────────────────────┘             │
└──────────────┬─────────────────────────────────────────────┘
               │ (SQL)
┌──────────────▼─────────────────────────────────────────────┐
│          POSTGRESQL DATABASE                                │
│  ┌──────────────────────────────────────────────┐          │
│  │ Users | Courses | Assessments | Mastery...   │          │
│  └──────────────────────────────────────────────┘          │
└──────────────────────────────────────────────────────────┘
```

## Key Components

### 1. **Mastery Engine**
- **Location**: `backend/app/engines/mastery_engine.py`
- **Algorithm**: Knowledge Tracing
- **Function**: Tracks and updates student concept mastery (0-100)
- **Input**: Assessment scores, problem difficulty, correctness
- **Output**: Updated mastery profile, weak concepts, adaptive homework

### 2. **Engagement Engine**
- **Location**: `backend/app/engines/engagement_engine.py`
- **Metrics**: 
  - Explicit participation (polls, responses)
  - Implicit engagement (confusion index)
- **Output**: Engagement index (0-100), at-risk students, class summary

### 3. **API Layer**
- **Students**: Profile, mastery, assignments
- **Teachers**: Dashboard, polls, student insights
- **Assessments**: Submit and track results
- **Engagement**: Track and aggregate data
- **Mastery**: Update scores, generate homework

### 4. **Data Models**
- **Users**: Students, teachers, admins
- **Assessments**: Test scores, concept-wise performance
- **MasteryProfiles**: Per-concept mastery tracking
- **EngagementRecords**: Poll responses, confusion metrics
- **Projects**: PBL management and tracking
- **HomeworkAssignments**: Adaptive practice problems

## Data Flow

### Assessment Flow
```
Student Takes Test
    ↓
Submit Assessment (/assessments/submit)
    ↓
Mastery Engine Updates Score
    ↓
Generate Weak Concept List
    ↓
Create Adaptive Homework (/mastery/generate-homework)
    ↓
Homework Presented to Student
```

### Engagement Flow
```
Teacher Creates Poll (/teachers/poll/create)
    ↓
Students Respond (explicit) + Camera tracks confusion (implicit)
    ↓
Track Engagement (/engagement/track)
    ↓
Engagement Engine Aggregates Data
    ↓
Dashboard Shows Real-time Metrics (/teachers/dashboard)
    ↓
Teacher Takes Action (intervention, reteach)
```

### Adaptive Learning Flow
```
Student Completes Assignment
    ↓
Mastery Score Updated
    ↓
Identify Weak Areas (<70 mastery)
    ↓
Calculate ZPD Level (1-5 difficulty)
    ↓
Generate Next Assignment at ZPD+1
    ↓
Present to Student
```

## Database Schema

### Core Tables
- **users**: All platform users
- **courses**: Course definitions
- **assessments**: Individual assessment results
- **mastery_profiles**: Per-student, per-concept mastery tracking
- **engagement_records**: Real-time engagement data points
- **projects**: PBL projects
- **pbl_teams**: Project team compositions
- **homework_assignments**: Adaptive homework tasks

### Indexes
- `users.email` - Fast user lookup
- `assessments.student_id` - Quick assessment retrieval
- `mastery_profiles(student_id, concept)` - Efficient mastery queries
- `engagement_records.student_id` - Fast engagement history

## API Response Format

All endpoints follow standard REST conventions:

### Success Response (200)
```json
{
  "data": {...},
  "message": "Success message",
  "status": "success"
}
```

### Error Response (4xx/5xx)
```json
{
  "error": "Error message",
  "status": "error",
  "code": "ERROR_CODE"
}
```

## Performance Considerations

1. **Database Indexing**: Critical queries on student_id and concept
2. **Caching**: Engagement metrics cached for 5-minute intervals
3. **Batch Operations**: Homework generation processes in bulk
4. **Query Optimization**: Specific field selection to minimize data transfer

## Security

1. **Authentication**: To be implemented (JWT recommended)
2. **Authorization**: Role-based access control (student/teacher/admin)
3. **Data Privacy**: Anonymous poll responses, encrypted assessments
4. **Input Validation**: Pydantic models validate all API inputs

## Scalability

- **Horizontal Scaling**: Stateless FastAPI allows load balancing
- **Database Sharding**: Can shard by institution or course
- **Caching Layer**: Redis for engagement metrics caching
- **Async Operations**: Homework generation runs asynchronously

## Next Steps for MVP

1. ✓ Project structure and core models
2. [ ] Database connection and migrations
3. [ ] Authentication system (JWT)
4. [ ] Frontend-Backend API integration
5. [ ] Camera-based confusion detection
6. [ ] Real-time WebSocket for live polls
7. [ ] PBL template library
8. [ ] Analytics dashboard
9. [ ] Reporting system
10. [ ] Deployment (Docker + Cloud)

---

**Version**: 0.1.0 (Alpha)  
**Last Updated**: January 1, 2026
