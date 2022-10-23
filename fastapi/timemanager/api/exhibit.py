from logging import getLogger

from timemanager.models import Exhibit
from timemanager.schemas import UpdateExhibitSchema

from fastapi import HTTPException, Request

logger = getLogger(__name__)


class ExhibitAPI:
    @classmethod
    def get(cls, request: Request) -> Exhibit:
        exhibit = Exhibit.objects.filter(uuid=request.user.exhibit.uuid).first()
        if not exhibit:
            raise HTTPException(status_code=404, detail="No such exhibit")
        return exhibit

    @classmethod
    def update(cls, request: Request, schema: UpdateExhibitSchema) -> Exhibit:
        exhibit, _ = Exhibit.objects.update_or_create(
            uuid=request.user.exhibit.uuid, defaults=schema.dict()
        )
        return exhibit
