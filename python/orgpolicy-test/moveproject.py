from google.cloud import resourcemanager_v3
from google.protobuf.field_mask_pb2 import FieldMask

def move_project(project_id, destination_org_id):

    client = resourcemanager_v3.ProjectsClient()

    # Get the project details
    project_name = f"projects/{project_id}"
    project = client.get_project(name=project_name)

    # Update the parent to the destination organization
    project.parent = f"organizations/{destination_org_id}"

    # Create a FieldMask for the fields to update
    update_mask = FieldMask(paths=["parent"])

    # Send the update request
    try:
        operation = client.update_project(project=project, update_mask=update_mask)
        print(f"Moving project '{project_id}' to organization '{destination_org_id}'...")

        # Wait for the operation to complete
        operation.result()
        print(f"Project '{project_id}' successfully moved to organization '{destination_org_id}'.")
    except Exception as e:
        print(f"Failed to move project: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your project ID and destination organization ID
    project_id = "your-project-id"
    destination_org_id = "your-destination-org-id"

    move_project(project_id, destination_org_id)


##############################
##############################
##############################


from google.cloud import resourcemanager_v3

def move_project(project_id, destination_org_id):
    """
    Moves a project from its current organization or folder to a new organization.

    Args:
        project_id (str): The ID of the project to move.
        destination_org_id (str): The ID of the destination organization.
    """
    client = resourcemanager_v3.ProjectsClient()

    # Get the project details
    project_name = f"projects/{project_id}"
    project = client.get_project(name=project_name)

    # Update the parent to the destination organization
    project.parent = f"organizations/{destination_org_id}"

    # Send the update request
    try:
        operation = client.update_project(project=project)
        print(f"Moving project '{project_id}' to organization '{destination_org_id}'...")

        # Wait for the operation to complete
        operation.result()
        print(f"Project '{project_id}' successfully moved to organization '{destination_org_id}'.")
    except Exception as e:
        print(f"Failed to move project: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your project ID and destination organization ID
    project_id = "your-project-id"
    destination_org_id = "your-destination-org-id"

    move_project(project_id, destination_org_id)
