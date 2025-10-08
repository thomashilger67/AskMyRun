import requests
from core.utils import get_delta_timestamp
from dotenv import load_dotenv
import os
import pandas as pd 
load_dotenv()

access_token = os.getenv("STRAVA_ACCESS_TOKEN")
headers= {'Authorization': 'Bearer ' + access_token} 


one_month_ago_timestamp = get_delta_timestamp(1,"months")


repsonse = requests.get(f"https://www.strava.com/api/v3/athlete/activities?after={one_month_ago_timestamp}&per_page=30",headers=headers)

data = repsonse.json()


desired_keys = ['id','name','distance','moving_time','elapsed_time','total_elevation_gain',
                'type','start_date','average_speed','max_speed', 'average_cadence',
                'average_watts','max_watts','weighted_average_watts','average_heartrate','max_heartrate',
                'elev_high','elev_low','calories']

filtered_data = [
    {k: activity[k] for k in desired_keys if k in activity}
    for activity in data
]

df_activities = pd.DataFrame(filtered_data)

