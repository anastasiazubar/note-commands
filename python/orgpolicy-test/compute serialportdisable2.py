from google.cloud import compute_v1

def enable_serial_port(project_id, zone, instance_name):
    # Initialize the client
    client = compute_v1.InstancesClient()

    # Get the current instance
    instance = client.get(project=project_id, zone=zone, instance=instance_name)
    
    # Use the existing metadata object
    metadata = instance.metadata
    
    # Add or overwrite the `serial-port-enable` key
    metadata.items.append(
        compute_v1.types.Metadata.Items(key="serial-port-enable", value="true")
    )

    # Update the instance metadata
    operation = client.set_metadata(
        project=project_id,
        zone=zone,
        instance=instance_name,
        metadata=metadata
    )

    # Wait for the operation to complete
    operation_client = compute_v1.ZoneOperationsClient()
    result = operation_client.wait(project=project_id, zone=zone, operation=operation.name)

    if result.error:
        print(f"Failed to update metadata: {result.error}")
    else:
        print(f"Serial port enabled for instance: {instance_name}")

# Usage example
project_id = "your-project-id"
zone = "your-zone"  # e.g., "us-central1-a"
instance_name = "your-instance-name"

enable_serial_port(project_id, zone, instance_name)

