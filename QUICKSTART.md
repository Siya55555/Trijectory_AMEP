# AMEP Quick Start Guide

## Project Overview

AMEP (Adaptive Mastery & Engagement Platform) is a unified educational platform that:
- Tracks student concept mastery dynamically
- Measures real-time engagement (polls + confusion detection)
- Generates personalized homework based on weaknesses
- Manages project-based learning with team collaboration
- Provides teachers with actionable insights

## Folder Structure

```
AMEP/
├── frontend/          → React/Next.js UI
├── backend/           → FastAPI REST APIs
├── database/          → PostgreSQL schema
├── docs/              → Documentation
└── README.md          → Main documentation
```

## Quick Setup

### Backend (5 minutes)

```bash
cd backend

# 1. Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure database
# Update DATABASE_URL in .env
cp .env.example .env

# 4. Create database schema
# Run schema.sql in your PostgreSQL client

# 5. Seed sample data (optional)
python seed.py

# 6. Run server
python main.py
```

**Server will be at**: `http://localhost:8000`  
**API Docs**: `http://localhost:8000/docs` (Swagger UI)

### Frontend (5 minutes)

```bash
cd frontend

# 1. Install dependencies
npm install

# 2. Run development server
npm run dev
```

**Frontend will be at**: `http://localhost:3000`

## Testing the APIs

### Using Curl

```bash
# Get student mastery profile
curl http://localhost:8000/api/students/1/mastery

# Create engagement record
curl -X POST http://localhost:8000/api/engagement/track \
  -H "Content-Type: application/json" \
  -d '{
    "student_id": 1,
    "course_id": 1,
    "poll_response": {"q1": "agree"},
    "confusion_index": 25,
    "participation_type": "explicit"
  }'

# Generate adaptive homework
curl -X POST http://localhost:8000/api/mastery/1/generate-homework
```

### Using Postman

1. Import the API documentation from `docs/API_DOCUMENTATION.md`
2. Create requests for each endpoint
3. Test with sample student IDs (1-5 from seed data)

## Key Features to Build

### Phase 1: Core (MVP)
- [x] Database schema and models
- [x] Basic CRUD APIs
- [x] Mastery Engine (Knowledge Tracing)
- [x] Engagement Engine
- [ ] Frontend-Backend integration
- [ ] Authentication/Login

### Phase 2: Enhanced
- [ ] Camera-based confusion detection
- [ ] Real-time WebSocket polls
- [ ] PBL template library
- [ ] Peer review system
- [ ] Advanced analytics dashboard

### Phase 3: Production
- [ ] Data export/reporting
- [ ] Multi-institutional support
- [ ] Mobile app
- [ ] AI-powered insights
- [ ] Cloud deployment

## Important Files

| File | Purpose |
|------|---------|
| `backend/app/models.py` | SQLAlchemy database models |
| `backend/app/engines/mastery_engine.py` | Knowledge Tracing algorithm |
| `backend/app/engines/engagement_engine.py` | Engagement analytics |
| `backend/app/api/` | All API endpoints |
| `database/schema.sql` | PostgreSQL schema |
| `frontend/app/student/page.tsx` | Student portal UI |
| `frontend/app/teacher/page.tsx` | Teacher dashboard UI |

## Environment Variables

Create `.env` file in backend directory:

```env
DATABASE_URL=postgresql://user:password@localhost/amep_db
DEBUG=True
API_TITLE=AMEP API
```

## Database Setup

### Using PostgreSQL

```sql
-- Create database
CREATE DATABASE amep_db;

-- Run schema
\c amep_db
\i database/schema.sql

-- Verify tables
\dt
```

## Useful Commands

```bash
# Backend - Install new packages
pip install package_name
pip freeze > requirements.txt

# Frontend - Install new packages
npm install package_name

# Format code
# Backend: python -m black .
# Frontend: npm run lint

# Run tests (when added)
# Backend: pytest
# Frontend: npm test
```

## Common Issues

### "Connection refused to database"
- Check PostgreSQL is running
- Verify DATABASE_URL in .env
- Run schema.sql to create tables

### "Module not found" errors
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`
- Check Python path in IDE

### Frontend not connecting to backend
- Backend must be running on localhost:8000
- Check CORS is enabled in main.py
- Verify API URLs match between frontend and backend

## API Endpoints Summary

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/students/{id}/mastery` | Get mastery profile |
| GET | `/api/students/{id}/assignments` | Get homework |
| POST | `/api/mastery/update` | Update mastery score |
| POST | `/api/mastery/{id}/generate-homework` | Create adaptive homework |
| POST | `/api/engagement/track` | Track engagement |
| GET | `/api/engagement/class/{cid}/summary` | Class engagement |
| GET | `/api/teachers/{id}/dashboard` | Teacher dashboard |
| POST | `/api/teachers/{id}/poll/create` | Create poll |
| POST | `/api/assessments/submit` | Submit assessment |

## Architecture Diagram

```
┌─────────────────────────────┐
│   Student/Teacher/Admin UI  │  (Next.js React)
└────────────┬────────────────┘
             │ HTTP/JSON
┌────────────▼────────────────┐
│   FastAPI REST Server       │
│  ├─ Mastery Engine          │
│  ├─ Engagement Engine        │
│  └─ PBL Manager             │
└────────────┬────────────────┘
             │ SQL
┌────────────▼────────────────┐
│  PostgreSQL Database        │
│  ├─ Users                   │
│  ├─ Assessments             │
│  ├─ Mastery Profiles        │
│  └─ Engagement Records      │
└─────────────────────────────┘
```

## Next Steps

1. Start backend and test APIs with Swagger UI
2. Connect frontend to backend
3. Implement authentication
4. Add real-time features (WebSocket)
5. Build camera integration for confusion detection
6. Deploy to cloud (Heroku, AWS, GCP)

## Help & Support

- **API Docs**: `http://localhost:8000/docs`
- **Architecture**: See `ARCHITECTURE.md`
- **Database**: See `database/schema.sql`
- **Full Docs**: See `README.md`

---

**Team**: Trivengers  
**Project**: Trajectory  
**Version**: 0.1.0
