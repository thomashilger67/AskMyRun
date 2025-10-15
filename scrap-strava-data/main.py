import requests
from core.utils import week_boundaries, to_pace
from dotenv import load_dotenv
import os
import pandas as pd 
from io import BytesIO
from google.cloud import storage


load_dotenv()

access_token = os.getenv("STRAVA_ACCESS_TOKEN")
date = os.getenv("DATE")
headers= {'Authorization': 'Bearer ' + access_token} 


after, before = week_boundaries(date)

repsonse = requests.get(f"https://www.strava.com/api/v3/athlete/activities?before={before}&after={after}&per_page=200",headers=headers)

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

##### Some transformations #####

df_activities['distance']= df_activities['distance'] / 1000  # Convert to kilometers
df_activities['moving_time']= df_activities['moving_time'].apply(lambda x: x / 60 if x else 0)   # Convert to minutes
df_activities['elapsed_time']= df_activities['elapsed_time'].apply(lambda x: x / 60 if x else 0)  # Convert to minutes
df_activities['average_speed'] =  df_activities['average_speed']  *3.6  # speed in Km/H

df_activities['pace'] =  df_activities['average_speed'].apply(to_pace) # Pace in min/km


#df_activities.to_json(f"{date}.parquet", index=False)
storage_client = storage.Client()
bucket = storage_client.bucket("strava_raw_data")


buffer = BytesIO()
df_activities.to_json(buffer, orient="records", lines=True, date_format="iso", compression="gzip")
buffer.seek(0)


blob = bucket.blob(f"{date}.json.gz")
blob.upload_from_file(buffer, content_type="application/gzip")


