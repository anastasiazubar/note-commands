from google.cloud import artifactregistry_v1beta2
from google.auth import default

# Set your project ID and location
project_id = 'your-project-id'
location = 'us-central1'

# Create a client
client = artifactregistry_v1beta2.ArtifactRegistryClient()

# Construct the parent resource name
parent = f"projects/{project_id}/locations/{location}"

# Construct the Artifact Registry to create
registry = {
    "name": f"{parent}/repositories/example-repo",
    "description": "Example Artifact Registry Repository",
    "format": "DOCKER"
}

# Create the Artifact Registry
response = client.create_repository(parent=parent, repository=registry)

print(f"Created Artifact Registry: {response.name}")
