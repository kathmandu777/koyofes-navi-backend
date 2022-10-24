from logging import getLogger

from fastapi import Request

from ..models import WaitingTime
from ..schemas import CreateWaitingTimeSchema

logger = getLogger(__name__)


class WaitingTimeAPI:
    @classmethod
    def create(cls, request: Request, schema: CreateWaitingTimeSchema) -> WaitingTime:
        waiting_time = WaitingTime.objects.create(
            exhibit_id=request.user.exhibit.uuid,
            minutes=schema.minutes,
            type=schema.type,
        )
        return waiting_time
