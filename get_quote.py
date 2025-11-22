import requests
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Now you can access the environment variables
access_token = os.getenv("API_TOKEN")


url = "https://gw-napi.kotaksecurities.com/apim/quotes/1.0/quotes/neosymbol/nse_cm%7C2885%2Cbse_cm%7C532174%2Cnse_fo%7C65500%2Cbse_cm%7C540376/all"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': f"Bearer {access_token}"
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
