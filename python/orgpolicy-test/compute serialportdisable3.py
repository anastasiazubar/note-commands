from google.auth import compute_engine
from googleapiclient import discovery

# Initialize the Compute Engine API client
credentials = compute_engine.Credentials()
service = discovery.build('compute', 'v1', credentials=credentials)

# Specify your project, zone, and instance
project = 'your-project-id'
zone = 'your-zone'
instance = 'your-instance-name'

# Define the metadata to update
metadata = {
    'items': [
        {'key': 'your-metadata-key', 'value': 'your-new-metadata-value'}
    ]
}

# Get the current metadata
instance_metadata = service.instances().get(
    project=project,
    zone=zone,
    instance=instance
).execute()

# Add or modify the metadata
instance_metadata['metadata']['items'].append({
    'key': 'your-metadata-key',
    'value': 'your-new-metadata-value'
})

# Update the metadata
request = service.instances().setMetadata(
    project=project,
    zone=zone,
    instance=instance,
    body=instance_metadata['metadata']
)

# Execute the request
response = request.execute()

print(f'Metadata updated: {response}')
