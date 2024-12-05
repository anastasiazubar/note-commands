from google.auth import compute_engine
from googleapiclient import discovery

# Initialize the Compute Engine API client
credentials = compute_engine.Credentials()
service = discovery.build('compute', 'v1', credentials=credentials)

# Specify your project, zone, and instance
project = 'your-project-id'
zone = 'your-zone'
instance = 'your-instance-name'

# Step 1: Get current metadata to retrieve the fingerprint
instance_metadata = service.instances().get(
    project=project,
    zone=zone,
    instance=instance
).execute()

# Extract the fingerprint from the current metadata
fingerprint = instance_metadata['metadata']['fingerprint']

# Step 2: Define the new metadata
metadata = {
    'fingerprint': fingerprint,  # Include the fingerprint from the current metadata
    'items': [
        {'key': 'your-new-metadata-key', 'value': 'your-new-metadata-value'}
    ]
}

# Step 3: Update the metadata
request = service.instances().setMetadata(
    project=project,
    zone=zone,
    instance=instance,
    body=metadata
)

# Execute the request
response = request.execute()

print(f'Metadata updated: {response}')
