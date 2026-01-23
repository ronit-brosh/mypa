from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from fastapi.middleware.cors import CORSMiddleware

from core.models import DayRequest
from core.planner import plan_day, load_wakeup_times


app = FastAPI()
print("🔥 THIS IS THE APP WITH CORS 🔥")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent





@app.get("/")
def root():
    return {"status": "mypa backend alive"}

@app.post("/plan/day")
def plan_day_endpoint(req: DayRequest):
    return plan_day(req,base_dir=BASE_DIR)



@app.get("/wakeup-times")
def get_wakeup_times():
    return load_wakeup_times(base_dir=BASE_DIR)


@app.get("/__cors_test")
def cors_test():
    return {"ok": True}


@app.get("/__whoami")
def whoami():
    return {"app": "api.py"}
