from datetime import datetime, timezone, timedelta
from logging import getLogger

from fastapi import Request

from ..models import Prize

logger = getLogger(__name__)

JST = timezone(timedelta(hours=+9), "JST")


class PrizeAPI:
    @classmethod
    def gets(cls, request: Request) -> list[Prize]:
        """11/5ならばis_first_day=TrueのPrizeを返す。11/6ならばis_second_day=TrueのPrizeを返す"""
        prizes = []

        if datetime.now(JST).day == 5:
            prize_candidates = Prize.objects.filter(is_first_day=True)
        elif datetime.now(JST).day == 6:
            prize_candidates = Prize.objects.filter(is_second_day=True)
        for prize in prize_candidates:
            prize.image_url = (
                prize.image.url if prize.image else None
            )  # FIXME: pydanticをスマートに使用して解消したいs
            prizes.append(prize)
        return prizes
