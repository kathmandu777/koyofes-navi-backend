from logging import getLogger

from fastapi import Request

from ..models import Prize

logger = getLogger(__name__)


class PrizeAPI:
    @classmethod
    def gets(cls, request: Request) -> list[Prize]:
        prizes = []
        for prize in Prize.objects.all():
            prize.image_url = (
                prize.image.url if prize.image else None
            )  # FIXME: pydanticをスマートに使用して解消したいs
            prizes.append(prize)
        return prizes
