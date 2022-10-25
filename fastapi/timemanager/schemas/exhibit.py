from pydantic import BaseModel, Field

from ..models import Exhibit
from .place import ReadPlaceSchema
from .waiting_time import ReadWaitingTimeSchema


class UpdateExhibitSchema(BaseModel):
    description: str = Field(
        ..., title="説明文", max_length=Exhibit.MAX_LENGTH_DESCRIPTION
    )

    class Config:
        orm_mode = True


class ReadExhibitSchema(BaseModel):
    name: str
    image_url: str | None
    description: str = ""
    places: list[ReadPlaceSchema] = []
    latest_waiting_time: ReadWaitingTimeSchema | None = None

    class Config:
        orm_mode = True
