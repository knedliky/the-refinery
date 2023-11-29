import json
from datetime import datetime


def lambda_handler(event, context):
    url = f"https://history.openweathermap.org/data/2.5/aggregated/month?lat={lat}&lon={lon}&month={month}&appid={key}"
    month = datetime.now().month
    return {"status_code": 200, "body": json.dumps(event)}
