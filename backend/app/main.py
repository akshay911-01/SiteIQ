from fastapi import FastAPI

from app.api.sites import router as sites_router



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
