from typing import List, Optional

from pydantic import BaseModel, Field


class Measurement(BaseModel):
    user_id: int = Field(alias='userId')
    words: List[str]
    said_words: List[Optional[str]] = Field(alias='saidWords')
    timings: List[Optional[int]]
    accuracy: float

    class Config:
        orm_mode = True
