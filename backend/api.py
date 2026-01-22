from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from core.scheduler import Block, build_schedule, reanchor_schedule
from fastapi.middleware.cors import CORSMiddleware
from core.google_calendar import get_calendar_events


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # MVP בלבד!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class DayRequest(BaseModel):
    date: str
    planned_wakeups: dict
    actual_wakeup: str | None = None


def day_key(date_str):
    d = date.fromisoformat(date_str)
    return d.strftime("%a").lower()[:3]

@app.get("/")
def root():
    return {"status": "mypa backend alive"}



@app.post("/plan/day")
def plan_day(req: DayRequest):
    day = day_key(req.date)
    planned = req.planned_wakeups[day]

    blocks = [
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

        # פגישה קבועה (אילוץ חיצוני)
        Block("פגישה", 0, 60, fixed_time="10:00"),
    ]

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


    schedule = build_schedule(req.date, planned, blocks)

    if req.actual_wakeup:
        schedule = reanchor_schedule(
            schedule,
            req.date,
            planned,
            req.actual_wakeup
        )

    return {
        "schedule": [
            {
                "name": b.name,
                "start": b.start.strftime("%H:%M"),
                "end": b.end.strftime("%H:%M")
            }
            for b in schedule
        ]
    }
