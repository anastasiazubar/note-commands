from google.auth import default
from googleapiclient.discovery import build

def create_essential_contact(organization_id, email, notification_category):
    """Creates an essential contact for a Google Cloud organization."""
    credentials, _ = default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    service = build("essentialcontacts", "v1", credentials=credentials)
    
    parent = f"organizations/{organization_id}"
    contact_body = {
        "email": email,
        "notificationCategorySubscriptions": [notification_category],
    }
    
    request = service.organizations().contacts().create(parent=parent, body=contact_body)
    response = request.execute()
    return response

# Example usage
if __name__ == "__main__":
    organization_id = "123456789"  # Replace with actual organization ID
    email = "user@example.com"  # Replace with actual email
    notification_category = "ALL"  # Replace with actual category (e.g., "SECURITY")








from googleapiclient import discovery
from google.auth import default

def create_contact_with_discovery():
    # Authenticate with default credentials
    credentials, _ = default()

    # Build the Essential Contacts API client
    service = discovery.build(
        "essentialcontacts", "v1", credentials=credentials
    )

    # Set your project ID
    project_id = "your-project-id"  # 🔁 Replace with your actual GCP project ID
    parent = f"projects/{project_id}"

    # Define the contact body
    contact_body = {
        "email": "test@test.co",
        "languageTag": "en-US",
        "notificationCategorySubscriptions": ["ALL"]
    }

    # Call the API to create the contact
    request = service.projects().contacts().create(
        parent=parent,
        body=contact_body
    )

    response = request.execute()

    # Print the response
    print("✅ Contact created:")
    print(f"Name: {response['name']}")
    print(f"Email: {response['email']}")
    print(f"Language: {response['languageTag']}")

if __name__ == "__main__":
    create_contact_with_discovery()
