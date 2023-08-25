import json
from datetime import datetime
import requests


def iss_position() -> tuple:
    result = requests.get("http://api.open-notify.org/iss-now.json",
                          timeout=10)
    data = json.loads(result.text)
    timestamp, longitude, latitide = data['timestamp'], \
        data['iss_position']['latitude'], \
        data['iss_position']['longitude']
    time_obj = datetime.fromtimestamp(timestamp)
    month = time_obj.month
    year = time_obj.year
    day = time_obj.day
    return (latitide, longitude, day, month, year)
