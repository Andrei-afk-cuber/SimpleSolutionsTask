import asyncio
from datetime import datetime, timezone, date
import logging

from sqlmodel import Session

from .celery_app import app
from .utils import get_many_currencies
from ..database import engine
from ..models.prices import Price

logger = logging.getLogger(__name__)


# get currency task
@app.task
def get_currency_task():
    time_utc = int(datetime.now(timezone.utc).timestamp())
    results = asyncio.run(get_many_currencies(['btc_usd', 'eth_usd']))

    saved, failed = [], []
    with Session(engine) as session:
        for ticker, price in results.items():
            if isinstance(price, Exception):
                failed.append(ticker)
                logging.error(f"{ticker}: {price}")
                continue
            session.add(
                Price(
                    ticker=ticker,
                    price=price,
                    time_utc_now=time_utc,
                    save_date=date.today()
                )
            )
            saved.append(ticker)
        session.commit()

    logger.info(f"Saved={saved} failed={failed}")
    return {"saved": saved, "failed": failed}