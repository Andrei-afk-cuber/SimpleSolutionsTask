from ..client.utils import get_many_currencies

async def test_get_many_currencies():
    results = await get_many_currencies(["btc_usd", "eth_usd"])

    assert isinstance(results, dict)
    assert "btc_usd" in results and "eth_usd" in results