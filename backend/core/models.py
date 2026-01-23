from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional
from pydantic import BaseModel
from typing import Optional

class DayRequest(BaseModel):
    date: str                      # "2026-01-23"
    actual_wakeup: Optional[str] = None

    

@dataclass
class Block:
    name: str
    offset_from_wakeup_min: int
    duration_min: int
    fixed_time: str | None = None
    start: datetime | None = None
    end: datetime | None = None





