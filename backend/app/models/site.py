from datetime import datetime
from sqlalchemy import DateTime, func, Float, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
class Site(Base):
    __tablename__= "sites"
    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,

    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,unique=True
    )
    location: Mapped[str]= mapped_column(
       
        String(255),
        nullable=False,
    )
    latitude: Mapped[float]= mapped_column(
        Float,
        nullable=False,
    )
    longitude:Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )
    created_at:Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )