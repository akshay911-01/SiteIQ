from fastapi import FastAPI
from app.models.site import Site
from app.database import Base,engine
from app.api.sites import router as sites_router
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="SiteIQ",
    description="AI-powered drone inspection intelligence platform",
    version="0.1.0",
)
app.include_router(sites_router)

@app.get("/health")
async def health_check():
    return {
        "status":"healthy",
        "service":"siteiq-api",

    }
