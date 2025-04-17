from googleapiclient import discovery
from google.auth import default

# Set project, zone, and VM instance
project = 'your-project-id'
zone = 'us-central1-a'
instance_name = 'your-instance-name'

# Get credentials and build the service
credentials, _ = default()
compute = discovery.build('compute', 'v1', credentials=credentials)

# Get the current instance metadata
instance = compute.instances().get(project=project, zone=zone, instance=instance_name).execute()
metadata = instance.get('metadata', {})
items = metadata.get('items', [])

# Check if 'serial-port-enable' already exists
serial_port_item = next((item for item in items if item['key'] == 'serial-port-enable'), None)
if serial_port_item:
    serial_port_item['value'] = 'TRUE'
else:
    items.append({'key': 'serial-port-enable', 'value': 'TRUE'})

# Update metadata fingerprint
metadata_body = {
    'fingerprint': metadata['fingerprint'],
    'items': items
}

# Set the metadata
operation = compute.instances().setMetadata(
    project=project,
    zone=zone,
    instance=instance_name,
    body=metadata_body
).execute()

print(f"Serial port access enabled: operation {operation['name']}")





-----------





from googleapiclient import discovery
from google.auth import default

project = 'your-project-id'
zone = 'us-central1-a'
instance_name = 'your-instance-name'

# Auth and client
credentials, _ = default()
compute = discovery.build('compute', 'v1', credentials=credentials)

# Get current metadata fingerprint
instance = compute.instances().get(project=project, zone=zone, instance=instance_name).execute()
fingerprint = instance['metadata']['fingerprint']

# Set new metadata (overwrite/add serial-port-enable)
metadata_body = {
    'fingerprint': fingerprint,
    'items': [
        {'key': 'serial-port-enable', 'value': 'TRUE'}
    ]
}

# Apply metadata update
operation = compute.instances().setMetadata(
    project=project,
    zone=zone,
    instance=instance_name,
    body=metadata_body
).execute()

print(f"Set serial-port-enable=TRUE — operation: {operation['name']}")

