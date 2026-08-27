from fastapi import FastAPI
from app.models.site import Site
from app.database import Base,engine

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="SiteIQ",
    description="AI-powered drone inspection intelligence platform",
    version="0.1.0",
)

@app.get("/health")
async def health_check():
    return {
        "status":"healthy",
        "service":"siteiq-api",

    }
