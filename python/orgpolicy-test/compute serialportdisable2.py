from google.cloud import compute_v1

def disable_serial_port_access(project_id, zone, instance_name):
    """
    Disables serial port access for a Google Compute Engine VM instance by updating metadata.

    Args:
        project_id (str): Your Google Cloud project ID.
        zone (str): The zone where the instance is located (e.g., "us-central1-a").
        instance_name (str): The name of the instance to update.
    """
    try:
        # Initialize the Instances client
        instances_client = compute_v1.InstancesClient()
        
        # Fetch the current instance metadata
        instance = instances_client.get(project=project_id, zone=zone, instance=instance_name)
        metadata = instance.metadata
        
        # Update metadata to disable serial port access
        new_metadata_items = metadata.items or []
        new_metadata_items.append(
            compute_v1.Metadata.Items(key="serial-port-enable", value="0")
        )
        
        # Set the updated metadata
        metadata.items = new_metadata_items
        operation = instances_client.set_metadata(
            project=project_id,
            zone=zone,
            instance=instance_name,
            metadata=metadata
        )
        operation.result()  # Wait for the operation to complete
        print(f"Serial port access successfully disabled for instance '{instance_name}'.")
    
    except Exception as e:
        print(f"Error disabling serial port access: {e}")

# Example usage
if __name__ == "__main__":
    project_id = "your-project-id"
    zone = "us-central1-a"
    instance_name = "your-instance-name"
    disable_serial_port_access(project_id, zone, instance_name)
