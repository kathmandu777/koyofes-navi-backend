from logging import getLogger

from fastapi import APIRouter, Depends, Request

from ..api import WaitingTimeAPI
from ..dependencies.auth import login_required
from ..models import WaitingTime
from ..schemas import CreateWaitingTimeSchema, ReadWaitingTimeSchema

logger = getLogger(__name__)
waiting_time_router = APIRouter()


@waiting_time_router.post(
    "/",
    response_model=ReadWaitingTimeSchema,
    dependencies=[Depends(login_required)],
)
async def create(request: Request, schema: CreateWaitingTimeSchema) -> WaitingTime:
    return WaitingTimeAPI.create(request, schema)
