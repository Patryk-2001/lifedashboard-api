import httpx

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

COINS = {
    "bitcoin": "Bitcoin",
    "ethereum": "Ethereum",
    "solana": "Solana"
}

async def get_crypto_prices():
    params = {
        "ids": ",".join(COINS.keys()),
        "vs_currencies": "eur,usd",
        "include_24hr_change": "true"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(COINGECKO_URL, params=params)
        response.raise_for_status()
        data = response.json()

    result = []
    for coin_id, coin_name in COINS.items():
        coin = data[coin_id]
        result.append({
            "nombre": coin_name,
            "precio_eur": coin["eur"],
            "precio_usd": coin["usd"],
            "cambio_24h": round(coin.get("eur_24h_change", 0), 2)
        })

    return result