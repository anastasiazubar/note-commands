from google.cloud import compute_v1

def disable_serial_port_access_simple(project_id, zone, instance_name):
    """
    Disables serial port access for a Google Compute Engine VM instance using minimal steps.

    Args:
        project_id (str): Your Google Cloud project ID.
        zone (str): The zone where the instance is located (e.g., "us-central1-a").
        instance_name (str): The name of the instance to update.
    """
    try:
        # Initialize the Instances client
        instances_client = compute_v1.InstancesClient()
        
        # Define new metadata with serial port disabled
        new_metadata = compute_v1.Metadata(items=[
            compute_v1.Metadata.Items(key="serial-port-enable", value="0")
        ])
        
        # Update the instance metadata
        operation = instances_client.set_metadata(
            project=project_id,
            zone=zone,
            instance=instance_name,
            metadata=new_metadata
        )
        operation.result()  # Wait for the operation to complete
        print(f"Serial port access successfully disabled for '{instance_name}'.")
    
    except Exception as e:
        print(f"Error disabling serial port access: {e}")

# Example usage
if __name__ == "__main__":
    project_id = "your-project-id"
    zone = "us-central1-a"
    instance_name = "your-instance-name"
    disable_serial_port_access_simple(project_id, zone, instance_name)
