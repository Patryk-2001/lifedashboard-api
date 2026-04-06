from fastapi import APIRouter, HTTPException
from app.services.finance import get_crypto_prices

router = APIRouter(prefix="/finance", tags=["Finance"])

@router.get("/crypto")
async def crypto_prices():
    try:
        return await get_crypto_prices()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))