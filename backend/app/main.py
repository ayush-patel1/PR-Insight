from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.github_webhook import router as github_webhook_router

# Create FastAPI application instance
app = FastAPI(
    title="PR Summary Bot",
    description="Backend service for GitHub PR summary and review context",
    version="1.0.0"
)

# Register routers
app.include_router(health_router)
app.include_router(github_webhook_router)