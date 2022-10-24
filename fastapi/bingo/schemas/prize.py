from logging import getLogger

from pydantic import BaseModel

logger = getLogger(__name__)


class ReadPrizeSchema(BaseModel):
    name: str
    count: int
    image_url: str | None

    class Config:
        orm_mode = True
