from datetime import date
import enum

from sqlmodel import SQLModel, Field


class Ticker(str, enum.Enum):
    btc_usd = "btc_usd"
    eth_usd = "eth_usd"


# DB price model
class Price(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    ticker: Ticker = Field(index=True)
    price: float = Field(..., gt=0)
    time_utc_now: int = Field(..., gt=0)
    save_date: date = Field(default=date.today(), index=True)