from google.cloud import compute_v1

def disable_serial_port_access(project_id, zone, instance_name):
    """
    Disables serial port access for a Google Compute Engine instance by updating metadata.

    Args:
        project_id (str): Your Google Cloud project ID.
        zone (str): The zone where the instance is located (e.g., "us-central1-a").
        instance_name (str): The name of the instance to update.
    """
    try:
        # Initialize the Instances client
        instances_client = compute_v1.InstancesClient()
        
        # Get the current instance metadata
        instance = instances_client.get(project=project_id, zone=zone, instance=instance_name)
        metadata = instance.metadata

        # Ensure metadata items are initialized
        if metadata.items is None:
            metadata.items = []
        
        # Update or add the 'serial-port-enable' key to metadata
        for item in metadata.items:
            if item.key == "serial-port-enable":
                item.value = "0"
                break
        else:
            metadata.items.append(compute_v1.Metadata.Items(key="serial-port-enable", value="0"))
        
        # Set the updated metadata
        operation = instances_client.set_metadata(
            project=project_id,
            zone=zone,
            instance=instance_name,
            metadata=metadata
        )
        operation.result()  # Wait for the operation to complete
        print(f"Serial port access disabled successfully for instance '{instance_name}'.")
    
    except Exception as e:
        print(f"Error disabling serial port access: {e}")

# Example usage
if __name__ == "__main__":
    project_id = "your-project-id"
    zone = "us-central1-a"
    instance_name = "your-instance-name"
    disable_serial_port_access(project_id, zone, instance_name)
