from aiohttp import ClientSession
import asyncio

# get currency by one ticker
async def get_currency(session: ClientSession, ticker: str):
    url = 'https://www.deribit.com/api/v2/public/get_index_price'
    params = {"index_name": ticker}
    async with session.get(url, params=params) as response:
        response.raise_for_status()
        data = await response.json()
        return data["result"]["index_price"]


# get currencies by many tickers
async def get_many_currencies(tickers: list):
    async with ClientSession() as session:
        results = await asyncio.gather(
            *[get_currency(session, ticker) for ticker in tickers],
            return_exceptions=True
        )

        return dict(zip(tickers, results))
