from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Import routers
from app.api import students, teachers, assessments, engagement, mastery

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("AMEP Backend Starting...")
    yield
    # Shutdown
    print("AMEP Backend Shutting Down...")

app = FastAPI(
    title="AMEP API",
    description="Adaptive Mastery & Engagement Platform API",
    version="0.1.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(students.router, prefix="/api/students", tags=["students"])
app.include_router(teachers.router, prefix="/api/teachers", tags=["teachers"])
app.include_router(assessments.router, prefix="/api/assessments", tags=["assessments"])
app.include_router(engagement.router, prefix="/api/engagement", tags=["engagement"])
app.include_router(mastery.router, prefix="/api/mastery", tags=["mastery"])

@app.get("/")
async def root():
    return {
        "message": "AMEP - Adaptive Mastery & Engagement Platform",
        "version": "0.1.0",
        "status": "running"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
