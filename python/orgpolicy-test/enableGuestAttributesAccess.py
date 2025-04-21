from googleapiclient import discovery
from google.auth import default

project = 'your-project-id'
zone = 'your-zone'  # e.g., 'us-central1-a'
instance = 'your-instance-name'

credentials, _ = default()
compute = discovery.build('compute', 'v1', credentials=credentials)

# Set metadata to enable guest attributes
metadata_body = {
    'items': [
        {
            'key': 'enable-guest-attributes',
            'value': 'TRUE'
        }
    ]
}

operation = compute.instances().setMetadata(
    project=project,
    zone=zone,
    instance=instance,
    body=metadata_body
).execute()

print(f"Guest attributes enabled. Operation ID: {operation['name']}")
