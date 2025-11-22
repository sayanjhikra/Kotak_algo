import requests
from dotenv import load_dotenv
import os
import pprint

load_dotenv()  # take environment variables from .env.

# Now you can access the environment variables
# consumer_key = os.getenv("CONSUMER_KEY")
# consumer_secret = os.getenv("CONSUMER_SECRET")
authorization = os.getenv("AUTHORIZATION")
username = os.getenv("API_USERNAME")
password = os.getenv("API_PASSWORD")
mobileNumber = os.getenv("PHONE")
mPin = os.getenv("M_PIN")


def save_token_to_env(key: str, token: str, env_file: str = ".env"):
    """Save or update a token in the .env file."""
    lines = []
    found = False

    # Read existing .env if it exists
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            lines = f.readlines()

    # Update if key already exists
    for i, line in enumerate(lines):
        if line.strip().startswith(f"{key}="):
            lines[i] = f"{key}={token}\n"
            found = True
            break

    # Add new key if not found
    if not found:
        lines.append(f"{key}={token}\n")

    # Write back to .env
    with open(env_file, "w") as f:
        f.writelines(lines)

    print(f"✅ Saved {key} to {env_file}")


headers = {
    'Authorization': 'Basic ' + authorization
}
data = {
    'grant_type': 'password',
    'username': username,
    'password': password
}
authT = requests.post("https://napi.kotaksecurities.com/oauth2/token", headers=headers, data=data)
# print(authT.json())

headers = {
    'Authorization': 'Bearer ' + authT.json()['access_token']
}
json_data = {
    'mobileNumber': mobileNumber,
    'mpin': mPin
}
login2 = requests.post("https://gw-napi.kotaksecurities.com/login/1.0/login/v2/validate",
                       headers=headers,
                       json=json_data)

headers = {
    'sid': login2.json()['data']['sid'],
    'Auth': login2.json()['data']['token'],
    'Authorization': 'Bearer ' + authT.json()['access_token']
}
json_data = {
    "rid": login2.json()['data']['rid'],
}

api_response = requests.post("https://gw-napi.kotaksecurities.com/login/1.0/login/refresh",
                          headers=headers,
                          json=json_data).json()
jwt_token= api_response['data']
pprint.pprint(jwt_token)

save_token_to_env("API_TOKEN", jwt_token['token'])
