from typing import List
from datetime import date

from .models import DayRequest, Block
from .scheduler import build_schedule, reanchor_schedule
from .google_calendar import get_calendar_events
from .utils import day_key
import json
from pathlib import Path
from typing import Dict

def load_wakeup_times(base_dir: Path) -> Dict[str, str]:
    path = base_dir / "data" / "wakeup_times.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def plan_day(req: DayRequest, base_dir: Path) -> dict:
    # ---- context בסיסי ----
    print("$$$$ Planning day for:", req.date)
    wakeup_times = load_wakeup_times(base_dir)
    print("$$$$ Loaded wakeup times:", wakeup_times)
    day = day_key(req.date)
    print("$$$$ Day key:", day)
    planned = wakeup_times[day]



    # ---- בלוקים בסיסיים (הרגלים + אילוצים ידועים) ----
    blocks: List[Block] = [
        # בוקר
        Block("ארגון הילדה + כלבה", 0, 40),

        # תוספים לפני קפה
        Block("תוספים 1–3 (לפני קפה)", 40, 5),

        # ספורט ומקלחת
        Block("ספורט", 50, 45),
        Block("מקלחת", 95, 20),

        # ארוחות + תוספים
        Block("ארוחת בוקר + תוספים 4–5", 120, 20),
        Block("ארוחת צהריים + תוסף 6", 300, 30),
        Block("ארוחת ערב + תוסף 7", 540, 30),

        # לפני שינה
        Block("תוסף 8 (לפני שינה)", 780, 5),

        # פגישה קבועה (אילוץ חיצוני ידוע)
        Block("פגישה", 0, 60, fixed_time="10:00"),
    ]

    # ---- אילוצים חיצוניים מהיומן ----
    calendar_events = get_calendar_events(req.date)

    for e in calendar_events:
        blocks.append(
            Block(
                name=f"📅 {e['name']}",
                offset_from_wakeup_min=0,
                duration_min=0,
                fixed_time=e["start"]
            )
        )

    # ---- בניית לו״ז ----
    schedule = build_schedule(
        req.date,
        planned,
        blocks
    )

    

    # ---- התאמה למציאות (קימה בפועל) ----

    if req.actual_wakeup:
        schedule = reanchor_schedule(
            schedule,
            req.date,
            planned,
            req.actual_wakeup
        )


    # ---- פלט API-friendly ----
    return {
        "schedule": [
            {
                "name": b.name,
                "start": b.start.strftime("%H:%M"),
                "end": b.end.strftime("%H:%M"),
            }
            for b in schedule
        ]
    }
