from google.cloud import compute_v1
from google.auth import compute_engine

# Initialize the client and credentials
client = compute_v1.InstancesClient(credentials=compute_engine.Credentials())
project = 'YOUR_PROJECT_ID'
zone = 'YOUR_ZONE'
instance = 'YOUR_INSTANCE_NAME'

# 1. Enable Serial Port on the instance by adding metadata
metadata = compute_v1.Metadata(
    items=[{
        'key': 'serial-port-enable',
        'value': 'true'
    }]
)

# Add metadata to enable serial port access
operation = client.set_metadata(
    project=project,
    zone=zone,
    instance=instance,
    metadata=metadata
)

# Wait for the operation to complete
operation.result()  # This will block until the operation completes

print(f"Serial port access enabled for {instance}.")

# 2. Fetch serial port output from port 1 (default port)
serial_output = client.get_serial_port_output(
    project=project,
    zone=zone,
    instance=instance,
    port=1  # Default port for serial output
)

# Print the serial port output (usually boot logs)
print("Serial Port Output:")
print(serial_output.contents)
