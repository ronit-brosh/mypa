from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional, List


@dataclass
class Block:
    name: str
    offset_from_wakeup_min: int
    duration_min: int
    fixed_time: Optional[str] = None


@dataclass
class ScheduledBlock:
    name: str
    start: datetime
    end: datetime


def build_schedule(
    day_date: str,
    planned_wakeup: str,
    blocks: List[Block]
):
    wakeup = datetime.fromisoformat(f"{day_date} {planned_wakeup}")
    schedule = []

    for b in blocks:
        if b.fixed_time:
            start = datetime.fromisoformat(f"{day_date} {b.fixed_time}")
        else:
            start = wakeup + timedelta(minutes=b.offset_from_wakeup_min)

        end = start + timedelta(minutes=b.duration_min)
        schedule.append(ScheduledBlock(b.name, start, end))

    return schedule


def reanchor_schedule(
    schedule: List[ScheduledBlock],
    day_date: str,
    planned_wakeup: str,
    actual_wakeup: str
):
    planned = datetime.fromisoformat(f"{day_date} {planned_wakeup}")
    actual = datetime.fromisoformat(f"{day_date} {actual_wakeup}")
    delta = actual - planned

    return [
        ScheduledBlock(
            b.name,
            b.start + delta,
            b.end + delta
        )
        for b in schedule
    ]
