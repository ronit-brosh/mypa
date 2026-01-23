from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel
from datetime import date

class DayRequest(BaseModel):
    date: date
    planned_wakeups: dict[str, str]
    actual_wakeup: str | None = None

@dataclass
class Block:
    name: str
    offset_from_wakeup_min: int
    duration_min: int
    fixed_time: str | None = None
    start: datetime | None = None
    end: datetime | None = None
