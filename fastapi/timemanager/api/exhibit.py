from logging import getLogger

from fastapi import Request

from ..models import Exhibit, WaitingTime
from ..schemas import UpdateExhibitSchema

logger = getLogger(__name__)


class ExhibitAPI:
    @classmethod
    def gets(cls, request: Request) -> list[Exhibit]:
        """Gets all exhibits."""
        exhibits = []
        for exhibit in Exhibit.objects.all():
            exhibit.latest_waiting_time = (
                WaitingTime.objects.filter(exhibit=exhibit)
                .order_by("-created_at")
                .first()
            )
            exhibit.places = list(exhibit.place_set.all())
            exhibits.append(exhibit)
            logger.debug(f"Exhibit: {vars(exhibit)}")
        return exhibits

    @classmethod
    def update(cls, request: Request, schema: UpdateExhibitSchema) -> Exhibit:
        exhibit, _ = Exhibit.objects.update_or_create(
            uuid=request.user.exhibit.uuid, defaults=schema.dict()
        )
        return exhibit
