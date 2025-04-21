from googleapiclient import discovery
from google.auth import default

project = 'your-project-id'
zone = 'your-zone'  # e.g. 'us-central1-a'
instance = 'your-instance-name'

credentials, _ = default()
compute = discovery.build('compute', 'v1', credentials=credentials)

# Enable Nested Virtualization
request_body = {
    "advancedMachineFeatures": {
        "enableNestedVirtualization": True
    }
}

operation = compute.instances().setMachineResources(
    project=project,
    zone=zone,
    instance=instance,
    body=request_body
).execute()

print(f"Nested virtualization enabled. Operation ID: {operation['name']}")
