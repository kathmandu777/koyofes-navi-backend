from pydantic import BaseModel, validator

from ..models.waiting_time import WaitingTimeType


class ReadWaitingTimeSchema(BaseModel):
    type: str
    minutes: int | None

    class Config:
        orm_mode = True


class CreateWaitingTimeSchema(BaseModel):
    type: WaitingTimeType
    minutes: int | None = None

    @validator("minutes")
    def validate_minutes(cls, v, values):
        if values["type"] == "IMMEDIATE" or values["type"] == "RESERVATION":
            if v is not None:
                raise ValueError("minutes must be None")
        else:
            if v is None:
                raise ValueError("minutes must not be None")
        return v
