from google.cloud import aiplatform

# Set your project ID, location, and endpoint ID
project_id = "your-project-id"
location = "us-central1"
endpoint_id = "your-endpoint-id"

# Initialize the AI Platform client
client_options = {"api_endpoint": f"{location}-aiplatform.googleapis.com"}
client = aiplatform.gapic.EndpointServiceClient(client_options=client_options)

# Define the endpoint name
endpoint_name = f"projects/{project_id}/locations/{location}/endpoints/{endpoint_id}"

# Define the updates to be applied to the endpoint
update_mask = {"paths": ["allow_load_balancing", "deployed_models"]}
allow_load_balancing = True  # Set to True if you want to allow load balancing, False otherwise
deployed_models = [  # List of DeployedModel IDs to be deployed on the endpoint
    {"id": "model-id-1", "machine_type": "n1-standard-4"},
    {"id": "model-id-2", "machine_type": "n1-standard-8"},
]

# Set the update request
update_request = aiplatform.gapic.UpdateEndpointRequest(
    endpoint=endpoint_name,
    endpoint=aiplatform.gapic.Endpoint(
        allow_load_balancing=allow_load_balancing,
        deployed_models=deployed_models,
    ),
    update_mask=update_mask,
)

# Patch the endpoint with the updates
response = client.update_endpoint(request=update_request)

# Display the response
print("Endpoint patched successfully:", response)
