from pydantic import BaseModel


class ReadWaitingTimeSchema(BaseModel):
    minutes: int

    class Config:
        orm_mode = True


class CreateWaitingTimeSchema(BaseModel):
    minutes: int
