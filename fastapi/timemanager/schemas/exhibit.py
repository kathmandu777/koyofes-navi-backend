from pydantic import BaseModel, Field
from timemanager.models import Exhibit


class UpdateExhibitSchema(BaseModel):
    description: str = Field(
        ..., title="説明文", max_length=Exhibit.MAX_LENGTH_DESCRIPTION
    )

    class Config:
        orm_mode = True


class ReadExhibitSchema(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True
