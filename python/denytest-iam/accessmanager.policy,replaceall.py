from google.oauth2 import service_account
from google.auth.transport.requests import Request
from googleapiclient import discovery

def replace_all_access_levels(project_id, access_policy_name, new_access_levels, service_account_file):
    # Load the service account credentials
    credentials = service_account.Credentials.from_service_account_file(
        service_account_file,
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )

    # Create the Access Context Manager service client
    access_context_manager = discovery.build(
        "accesscontextmanager",
        "v1",
        credentials=credentials,
        cache_discovery=False,
    )

    # Construct the request body
    request_body = {
        "accessLevels": new_access_levels
    }

    # Call the Access Context Manager API to replace all access levels
    try:
        response = access_context_manager.accessPolicies().patch(
            name=access_policy_name,
            updateMask="accessLevels",
            body=request_body
        ).execute()

        print("Access levels replaced successfully.")
    except Exception as e:
        print(f"Failed to replace access levels: {e}")

# Example usage
project_id = "your-project-id"
access_policy_name = "accessPolicies/your-access-policy-id"
new_access_levels = [
    {
        "name": "accessPolicies/your-access-policy-id/accessLevels/new-access-level-1",
        "title": "New Access Level 1",
        "basic": {
            "conditions": {
                "regions": ["your-region"],
                "ipSubnetworks": ["your-ip-subnetwork"],
                "members": ["user:your-user@example.com"]
            }
        }
    },
    # Add more access levels as needed
]
service_account_file = "path/to/your/service_account.json"

replace_all_access_levels(project_id, access_policy_name, new_access_levels, service_account_file)
