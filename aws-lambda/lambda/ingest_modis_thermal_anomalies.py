import json


def lambda_handlder(event, context):
    return {"status_code": "200", "body": json.loads(event)}
