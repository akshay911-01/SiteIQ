from fastapi import APIRouter,Depends,status
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.site import Site
from app.schemas.site import SiteCreate,SiteResponse

router= APIRouter(
    prefix="/sites",
    tags=["Sites"],
)
@router.post(
    "",
    response_model=SiteResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_site (
    site_data : SiteCreate,
    db: Session = Depends(get_db),
):
    site = Site(
        name=site_data.name,
        location=site_data.location,
        latitude=site_data.latitude,
        longitude=site_data.longitude,
    )

    db.add(site)
    db.commit()
    db.refresh(site)
    return site
@router.get(
    "",
    response_model=list[SiteResponse],

)
def get_sites(
    db: Session = Depends(get_db)
):
    result= db.execute(
        select(Site).order_by(Site.created_at.desc())
    )
    return result.scalars().all()