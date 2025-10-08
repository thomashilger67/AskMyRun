import requests
from utils import get_delta_timestamp
from dotenv import load_dotenv
import os

load_dotenv()

access_token = os.getenv("STRAVA_ACCESS_TOKEN")
headers= {'Authorization': 'Bearer ' + access_token} 


one_month_ago_timestamp = get_delta_timestamp(1,"weeks")

print(one_month_ago_timestamp)


repsonse = requests.get(f"https://www.strava.com/api/v3/athlete/activities?after={one_month_ago_timestamp}&per_page=50",headers=headers)

data = repsonse.json()
print([activity['name'] for activity in data])