from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import pickle

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def get_calendar_events(date_str):
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("calendar", "v3", credentials=creds)

    start = datetime.fromisoformat(date_str)
    end = start + timedelta(days=1)

    events_result = service.events().list(
        calendarId="primary",
        timeMin=start.isoformat() + "Z",
        timeMax=end.isoformat() + "Z",
        singleEvents=True,
        orderBy="startTime",
    ).execute()

    events = []
    for e in events_result.get("items", []):
        if "dateTime" in e["start"]:
            events.append({
                "name": e.get("summary", "Busy"),
                "start": e["start"]["dateTime"][11:16],
                "end": e["end"]["dateTime"][11:16],
            })

    return events
