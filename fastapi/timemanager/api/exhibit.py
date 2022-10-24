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

            places = []
            for place in exhibit.place_set.all():
                place.image = "/media/map/" + place.image  # FIXME: hard coding
                places.append(place)
            exhibit.places = places

            exhibit.image_url = (
                exhibit.image.url if exhibit.image else None
            )  # FIXME: pydanticをスマートに使用して解消したい
            exhibits.append(exhibit)
        return exhibits

    @classmethod
    def update(cls, request: Request, schema: UpdateExhibitSchema) -> Exhibit:
        exhibit, _ = Exhibit.objects.update_or_create(
            uuid=request.user.exhibit.uuid, defaults=schema.dict()
        )
        return exhibit
