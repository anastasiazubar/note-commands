from googleapiclient.discovery import build
from google.auth import default
from googleapiclient.errors import HttpError

def remove_all_liens(project_id):
    """
    Remove all liens from a Google Cloud project.

    Args:
        project_id (str): The ID of the Google Cloud project.
    """
    try:
        # Authenticate and initialize the Resource Manager API client
        credentials, _ = default()
        service = build('cloudresourcemanager', 'v3', credentials=credentials)

        # List all liens for the specified project
        parent = f"projects/{project_id}"
        print(f"Listing liens for project: {project_id}")
        
        request = service.liens().list(parent=parent)
        response = request.execute()

        # Check if liens exist
        liens = response.get('liens', [])
        if not liens:
            print("No liens found for the project.")
            return

        # Iterate through and delete each lien
        for lien in liens:
            lien_name = lien['name']  # Format: 'liens/{LIEN_ID}'
            print(f"Deleting lien: {lien_name}")

            try:
                service.liens().delete(name=lien_name).execute()
                print(f"Successfully deleted lien: {lien_name}")
            except HttpError as e:
                print(f"Failed to delete lien {lien_name}: {e}")

        print("All liens removed successfully.")

    except HttpError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Replace with your target project ID
    project_id = "your-project-id"
    remove_all_liens(project_id)
