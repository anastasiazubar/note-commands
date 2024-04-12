from google.cloud import aiplatform

# Set your project ID, location, and endpoint ID
project_id = "your-project-id"
location = "us-central1"
endpoint_id = "your-endpoint-id"

# Initialize the AI Platform client
aiplatform.init(project=project_id, location=location)

# Get the endpoint resource
endpoint = aiplatform.Endpoint(endpoint_name=f"projects/{project_id}/locations/{location}/endpoints/{endpoint_id}")

# Set the updates you want to apply to the endpoint
update_mask = {"allow_load_balancing", "deployed_models"}
allow_load_balancing = True  # Set to True if you want to allow load balancing, False otherwise
deployed_models = [  # List of DeployedModel IDs to be deployed on the endpoint
    {"id": "model-id-1", "machine_type": "n1-standard-4"},
    {"id": "model-id-2", "machine_type": "n1-standard-8"},
]

# Patch the endpoint with the updates
updated_endpoint = endpoint.patch(
    allow_load_balancing=allow_load_balancing,
    deployed_models=deployed_models,
    update_mask=update_mask,
)

# Display updated endpoint information
print("Endpoint patched successfully:", updated_endpoint)
