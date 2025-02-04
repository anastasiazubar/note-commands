from google.cloud import resourcemanager

# Replace with your project ID and service account email
PROJECT_ID = "your-project-id"
SERVICE_ACCOUNT_EMAIL = "your-sa-email@your-project-id.iam.gserviceaccount.com"
ROLE_TO_CHECK = "roles/editor"

def sa_has_role(project_id, sa_email, role):
    """Checks if a service account has a specific IAM role in the project."""
    client = resourcemanager.ProjectsClient()
    project_name = f"projects/{project_id}"

    policy = client.get_iam_policy(resource=project_name)

    for binding in policy.bindings:
        if role == binding.role and f"serviceAccount:{sa_email}" in binding.members:
            return True  # The service account has the role

    return False  # The service account does not have the role

if __name__ == "__main__":
    has_role = sa_has_role(PROJECT_ID, SERVICE_ACCOUNT_EMAIL, ROLE_TO_CHECK)
    if has_role:
        print(f"Service Account {SERVICE_ACCOUNT_EMAIL} HAS the role {ROLE_TO_CHECK}")
    else:
        print(f"Service Account {SERVICE_ACCOUNT_EMAIL} does NOT have the role {ROLE_TO_CHECK}")