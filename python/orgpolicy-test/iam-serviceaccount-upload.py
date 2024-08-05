###
# https://cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/upload
##

import json
import requests
from google.auth import default
from google.auth.transport.requests import Request

def upload_service_account_key(project_id, service_account_email, key_file_path):
    # Load the existing key from file
    with open(key_file_path, 'r') as key_file:
        key_data = json.load(key_file)

    # Set up the authentication
    credentials, _ = default()
    auth_request = Request()
    credentials.refresh(auth_request)
    access_token = credentials.token

    # Construct the URL
    url = f'https://iam.googleapis.com/v1/projects/{project_id}/serviceAccounts/{service_account_email}/keys:upload'

    # Prepare the request headers and payload
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        'key': key_data['key'],  # Assuming the key data includes the key field. Adjust based on your actual key format.
    }

    # Make the API request to upload the key
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print('Key uploaded successfully:')
        print(response.json())
    else:
        print('Failed to upload key:')
        print(response.status_code)
        print(response.text)

if __name__ == "__main__":
    project_id = 'your-project-id'
    service_account_email = 'your-service-account@your-project-id.iam.gserviceaccount.com'
    key_file_path = 'path/to/your/existing-key.json'

    upload_service_account_key(project_id, service_account_email, key_file_path)
