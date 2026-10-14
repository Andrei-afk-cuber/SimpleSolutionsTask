from fastapi import APIRouter


router = APIRouter()


# All saved data
@router.get("/prices")
def get_prices(ticker: str):
    pass


# Last currency price
@router.get("/prices/{currency}")
def get_price(currency: str, ticker: str):
    pass


# Currency prices by date
@router.get("/prices/{currency}")
def get_prices_by_date(currency_str: str, date: str, ticker: str):
    pass