from ..models.prices import Price

class TestAPI:
    def test_get_all_prices(self, client):
        response = client.get("/prices?ticker=btc_usd")

        assert response.status_code == 200
        assert response.json()[0]["ticker"] == "btc_usd"

        response = client.get("/prices?ticker=eth_usd")
        assert response.status_code == 200
        assert response.json()[0]["ticker"] == "eth_usd"

        response = client.get("/prices?ticker=error")
        assert response.status_code == 422


    def test_get_last_price(self, client):
        response = client.get("/last-price?ticker=btc_usd")

        assert response.status_code == 200
        assert "ticker" in response.json() and "price" in response.json()
        assert response.json()["ticker"] == "btc_usd"

        response = client.get("/last-price?ticker=eth_usd")

        assert response.status_code == 200
        assert "ticker" in response.json() and "price" in response.json()
        assert response.json()["ticker"] == "eth_usd"