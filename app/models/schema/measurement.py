from pydantic import BaseModel


class Measurement(BaseModel):
    id: int
    time: int
    value: str

    class Config:
        orm_mode = True
