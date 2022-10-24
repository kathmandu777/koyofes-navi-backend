from fastapi import APIRouter, Request

from ..api import PrizeAPI
from ..models import Prize
from ..schemas import ReadPrizeSchema

prize_router = APIRouter()


@prize_router.get("/", response_model=list[ReadPrizeSchema])
async def gets(request: Request) -> list[Prize]:
    return PrizeAPI.gets(request)
