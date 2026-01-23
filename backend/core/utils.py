from datetime import date


def day_key(date_str):
    d = date.fromisoformat(date_str)
    print("*********",d.strftime("%a").lower()[:3])
    return d.strftime("%a").lower()[:3]

