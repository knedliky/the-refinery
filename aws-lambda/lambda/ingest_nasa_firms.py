import os

import requests


def lambda_handler(event, context):
    date = "2023-11-06"
    country = "ZAF"
    source = "MODIS_NRT"
    map_key = os.environ.get("NASA_FIRMS_MAP_KEY")
    day_range = 1

    url = f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/{map_key}/{source}/{country}/{day_range}"
    if date:
        url = f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/{map_key}/{source}/{country}/{day_range}/{date}"
    response = requests.get(url)
    content = response.content.decode("utf-8")
    return {"status_code": 200, "body": content}


# Scheduled Events from CloudWatch should contain the following parameters:
# {
#   "date": "2020-11-06",
#   "country": "ZAF",
#   "source": "MODIS_NRT",
#   "day_range": 1
# }

# Response should write to S3 bucket
# country > source > date > csv
