from typing import Annotated
from datetime import date

from fastapi import APIRouter, Query
from sqlmodel import select, desc

from ..dependencies.database import SessionDep
from ..models.prices import Price, Ticker

router = APIRouter()


# All saved data
@router.get("/prices", response_model=list[Price])
def get_all_prices(
        session: SessionDep,
        date_str: Annotated[date | None, Query(alias="date")] = None,
        ticker: Ticker = Ticker.btc_usd
):
    stmt = select(Price).where(Price.ticker == ticker)
    # date filtering
    if date_str:
        stmt = stmt.where(Price.save_date == date_str)

    prices = session.exec(stmt).all()

    return prices


# Last currency price
@router.get("/last-price")
def get_price(session: SessionDep, ticker: Ticker = Ticker.btc_usd):
    price = session.exec(select(Price).where(Price.ticker == ticker).order_by(desc(Price.time_utc_now))).first()
    return price