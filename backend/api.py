from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from core.scheduler import Block, build_schedule, reanchor_schedule
from fastapi.middleware.cors import CORSMiddleware
from core.google_calendar import get_calendar_events

from backend.models import DayRequest
from backend.core.planner import plan_day



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
def plan_day_endpoint(req: DayRequest):
    return plan_day(req)

