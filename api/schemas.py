# api/schemas.py
from pydantic import BaseModel

class ChartInput(BaseModel):
    date_of_birth: str
    time_of_birth: str
    place_of_birth: str
