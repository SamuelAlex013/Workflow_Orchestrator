"""n8n Workflow Orchestrator API - AI-powered workflow generation."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .api.workflow_router import router as workflow_router, initialize_services


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting Workflow Orchestrator...")
    await initialize_services()
    print("✅ Ready")
    yield
    print("🛑 Shutting down...")


app = FastAPI(
    title="Workflow Orchestrator API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(workflow_router)


@app.get("/")
def root():
    return {"status": "ok", "version": "0.1.0"}

# Run with: uvicorn backend.app.main:app --host