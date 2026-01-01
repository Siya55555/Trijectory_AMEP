# AMEP - Adaptive Mastery & Engagement Platform

## Project Structure

```
AMEP/
├── frontend/               # React/Next.js Frontend
│   ├── app/
│   │   ├── page.tsx       # Home page
│   │   ├── student/       # Student portal
│   │   ├── teacher/       # Teacher dashboard
│   │   ├── admin/         # Admin portal
│   │   ├── layout.tsx
│   │   └── globals.css
│   ├── package.json
│   └── tsconfig.json
│
├── backend/               # FastAPI Backend
│   ├── app/
│   │   ├── api/
│   │   │   ├── students.py      # Student endpoints
│   │   │   ├── teachers.py      # Teacher endpoints
│   │   │   ├── assessments.py   # Assessment endpoints
│   │   │   ├── engagement.py    # Engagement tracking
│   │   │   └── mastery.py       # Mastery engine endpoints
│   │   ├── engines/
│   │   │   ├── mastery_engine.py       # Knowledge Tracing
│   │   │   └── engagement_engine.py    # Engagement Analytics
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models.py
│   │   └── __init__.py
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
│
├── database/              # Database Setup
│   └── schema.sql         # PostgreSQL schema
│
└── docs/                  # Documentation
```

## Key Features

### 1. **Adaptive Mastery Engine**
- Knowledge Tracing algorithm for concept mastery
- Tracks student performance across concepts (0-100 score)
- Dynamic homework generation based on weaknesses

### 2. **Engagement Analytics**
- Real-time poll integration
- Confusion index tracking (implicit engagement)
- Class-wide engagement metrics
- At-risk student identification

### 3. **Project-Based Learning Management**
- Team formation and management
- Milestone tracking
- Artifact submission system

### 4. **Teacher Dashboard**
- Real-time engagement metrics
- Student mastery visualization
- Confusion detection with intervention prompts
- PBL project monitoring

### 5. **Student Portal**
- Personalized mastery profiles
- Adaptive homework assignments
- PBL project collaboration workspace

## Backend API Endpoints

### Students
- `GET /api/students/{student_id}/mastery` - Get mastery profile
- `GET /api/students/{student_id}/assignments` - Get adaptive assignments

### Teachers
- `GET /api/teachers/{teacher_id}/dashboard` - Get class dashboard
- `POST /api/teachers/{teacher_id}/poll/create` - Create engagement poll
- `GET /api/teachers/{teacher_id}/poll/{poll_id}/results` - Get poll results

### Engagement
- `POST /api/engagement/track` - Track student engagement
- `GET /api/engagement/class/{course_id}/summary` - Get class engagement

### Mastery
- `POST /api/mastery/update` - Update mastery score
- `GET /api/mastery/{student_id}/weak-concepts` - Get weak areas
- `POST /api/mastery/{student_id}/generate-homework` - Generate adaptive homework

### Assessments
- `POST /api/assessments/submit` - Submit assessment

## Technology Stack

**Frontend:**
- Next.js 14
- React 18
- Tailwind CSS
- TypeScript

**Backend:**
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Python 3.9+

**Database:**
- PostgreSQL (Main DB)
- Firebase/Cloud Storage (Artifacts)
- Analytics DB (Trends & Metrics)

## Getting Started

### Backend Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up PostgreSQL database and update `.env`:
```bash
cp backend/.env.example backend/.env
# Update database URL in .env
```

4. Create database schema:
```bash
psql -U postgres -d amep_db -f database/schema.sql
```

5. Run backend:
```bash
python main.py
```

Backend will be available at `http://localhost:8000`

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Run development server:
```bash
npm run dev
```

Frontend will be available at `http://localhost:3000`

## Core Algorithms

### Knowledge Tracing (Mastery Engine)
- **Initial probability**: 0.5 (50% chance of correct answer)
- **Learning rate**: 0.1 per correct attempt
- **Difficulty weighting**: Harder problems provide more learning gain
- **Forgetting**: Slight penalty on incorrect answers

### Engagement Index
- **Participation Score**: Based on poll responses and interactions
- **Confusion Score**: Inverse of confusion index (lower confusion = higher engagement)
- **Weighted Average**: 60% participation + 40% confusion management

### Adaptive Homework Generation
- Identifies weak concepts (mastery < 70%)
- Generates problems one level above current weakness (Zone of Proximal Development)
- Difficulty: 1-5 scale based on mastery score

## Next Steps for Hackathon

1. Connect frontend to backend APIs
2. Implement camera-based confusion detection
3. Add real-time WebSocket for live polls
4. Integrate authentication system
5. Add PBL template library
6. Implement peer review system for soft-skill assessment
7. Add export/reporting features

---

**Team**: Trivengers  
**Project**: Trajectory (AMEP)  
**Hackathon**: Quasar 4.0
