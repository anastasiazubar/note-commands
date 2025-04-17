from googleapiclient import discovery
from google.auth import default

project = 'your-project-id'
zone = 'your-zone'  # e.g., 'us-central1-a'
instance = 'your-instance-name'
network_interface = 'nic0'  # default for most instances

credentials, _ = default()
compute = discovery.build('compute', 'v1', credentials=credentials)

# Body to attach an ephemeral external IP
access_config = {
    "name": "External NAT",
    "type": "ONE_TO_ONE_NAT"
}

# Add external IP access
operation = compute.instances().addAccessConfig(
    project=project,
    zone=zone,
    instance=instance,
    networkInterface=network_interface,
    body=access_config
).execute()

print(f"External IP access enabled. Operation ID: {operation['name']}")
