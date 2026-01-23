from datetime import date

def day_key(d: date) -> str:
    return d.strftime("%A").lower()
