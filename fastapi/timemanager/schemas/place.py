from pydantic import BaseModel


class ReadPlaceSchema(BaseModel):
    name: str
    image: str
    position_x: float
    position_y: float

    class Config:
        orm_mode = True
