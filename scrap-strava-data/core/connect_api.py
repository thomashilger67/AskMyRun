import requests
from dotenv import load_dotenv
import os
load_dotenv()


client_id = os.getenv("STRAVA_CLIENT_ID")
client_secret = os.getenv("STRAVA_CLIENT_SECRET")
client_refresh_token= "a7f2843fabb0bc306e809a74fe4470d579dc0743"

payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'authorization_code',
    'code': client_refresh_token
}
response = requests.post(url=f"https://www.strava.com/oauth/token", data=payload)


print(response.json())
print(response.json()['access_token'])