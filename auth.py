import requests
import json

def generate_and_save_auth_token(url, credentials, output_file):
    response = requests.post(url, json=credentials)
    response_data = response.json()
    auth_token = response_data.get('token')

    with open(output_file, 'w') as f:
        json.dump({'auth_token': auth_token}, f)
