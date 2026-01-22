# mypa 🧠⏱️  
**A personal, adaptive daily planner that actually reacts to your life**

mypa is an experimental personal assistant that builds a daily schedule around *how your day really starts*, not how you wished it would.

It combines:
- dynamic daily planning
- real personal habits
- live Google Calendar integration
- and a foundation for adaptive, agent-like behavior

This project started as a hands-on exploration of multi-agent thinking and quickly turned into a working product prototype.

---

## ✨ What mypa does (so far)

### 🕰️ Wakeup-aware daily planning
- Define a planned wakeup per day
- Enter your **actual wakeup time**
- The entire day schedule shifts accordingly

No guilt. No manual rearranging.

---

### 🔁 Habit-based blocks (with dependencies)
The schedule is built from real habits, not abstract tasks:
- Daily workout → shower
- Supplements based on *events* (before coffee, with meals, before sleep)
- Fixed routines (school prep, dog walk)

Blocks are ordered, dependent, and time-aware.

---

### 📅 Live Google Calendar integration (read-only)
- Reads meetings from your Google Calendar
- Injects them into the daily schedule as fixed blocks
- Respects existing commitments without manual copying

OAuth-based, local, and private.

---

### 🔄 Rebuild anytime
Change your wakeup time → rebuild the day → see the impact instantly.

---

## 🧠 What this is *not* (yet)

- Not a to-do list
- Not a calendar replacement
- Not another productivity guilt machine

mypa is intentionally focused on **adaptive structure**, not micromanagement.

---

## 🛠️ Tech stack

- **Backend**: Python, FastAPI
- **Frontend**: Plain HTML + JS (intentionally minimal)
- **Scheduling logic**: custom block-based planner
- **Calendar**: Google Calendar API (OAuth, read-only)
- **Infra**: local-first, no DB (yet)

---

## 🚀 Running locally

### Backend
```bash
cd backend
uvicorn api:app --reload
