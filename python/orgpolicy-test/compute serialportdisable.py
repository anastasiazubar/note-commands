from google.cloud import compute_v1

def disable_serial_port_access_project_level(project_id):
    """
    Disables serial port access for all instances in a project by updating common metadata.

    Args:
        project_id (str): Your Google Cloud project ID.
    """
    try:
        # Initialize the client
        client = compute_v1.ProjectsClient()

        # Set common metadata to disable serial port access
        metadata = compute_v1.Metadata(items=[
            compute_v1.Metadata.Items(key="serial-port-enable", value="0")
        ])
        
        # Apply the metadata to the project
        operation = client.set_common_instance_metadata(project=project_id, metadata=metadata)
        operation.result()  # Wait for the operation to complete
        print(f"Serial port access disabled for all instances in project '{project_id}'.")
    
    except Exception as e:
        print(f"Error disabling serial port access: {e}")

# Example usage
if __name__ == "__main__":
    project_id = "your-project-id"
    disable_serial_port_access_project_level(project_id)
