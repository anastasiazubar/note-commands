from googleapiclient import discovery
from google.auth import default

project = 'your-project-id'
zone = 'your-zone'  # e.g., 'us-east4-a'
instance = 'your-instance-name'

credentials, _ = default()
compute = discovery.build('compute', 'v1', credentials=credentials)

# Disable Shielded VM features
shielded_config = {
    "enableSecureBoot": False,
    "enableVtpm": False,
    "enableIntegrityMonitoring": False
}

operation = compute.instances().updateShieldedInstanceConfig(
    project=project,
    zone=zone,
    instance=instance,
    body={"shieldedInstanceConfig": shielded_config}
).execute()

print(f"Shielded VM features disabled. Operation ID: {operation['name']}")




from googleapiclient import discovery
from google.auth import default

project = 'your-project-id'
zone = 'your-zone'  # e.g., 'us-east4-a'
instance = 'your-instance-name'

credentials, _ = default()
compute = discovery.build('compute', 'v1', credentials=credentials)

operation = compute.instances().stop(
    project=project,
    zone=zone,
    instance=instance
).execute()

print(f"Stopping instance '{instance}'. Operation ID: {operation['name']}")
