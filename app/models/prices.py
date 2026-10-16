from sqlmodel import SQLModel, Field

from app.database import engine


# DB price model
class Price(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    ticker: str = Field(index=True)
    price: float = Field(..., gt=0)
    time_utc_now: int = Field(..., gt=0)