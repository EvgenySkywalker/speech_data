from fastapi import APIRouter

from app.models.db import session_scope, Measurement
from app.models.schema.measurement import Measurement as MeasurementSchema

router = APIRouter()


@router.post('/add_measurement')
async def add_measurement(data: MeasurementSchema):
    with session_scope() as session:
        time = data.timings[-1]
        wps = len(data.said_words) / time
        said_symbols = 0
        for word in data.said_words:
            said_symbols = len(word)
        sps = said_symbols / time
        session.add(
            Measurement(
                user_id=data.user_id,
                accuracy=data.accuracy,
                words=data.words,
                said_words=data.said_words,
                timings=data.timings,
                sps=sps,
                wps=wps,
            )
        )
