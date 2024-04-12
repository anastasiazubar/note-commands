from google.cloud import aiplatform

# Set your project ID, location, endpoint ID, and model ID
project_id = "your-project-id"
location = "us-central1"
endpoint_id = "your-endpoint-id"
model_id = "your-model-id"

# Initialize the AI Platform client
aiplatform.init(project=project_id, location=location)

# Get the model resource
model = aiplatform.Model(model_name=f"projects/{project_id}/locations/{location}/models/{model_id}")

# Get the endpoint resource
endpoint = aiplatform.Endpoint(endpoint_name=f"projects/{project_id}/locations/{location}/endpoints/{endpoint_id}")

# Deploy the model to the endpoint
deployed_model = endpoint.deploy(
    model=model,
    deployed_model_display_name="your-deployed-model-name",
    traffic_percentage=100,
)

# Display deployment information
print("Model deployed to endpoint with ID:", deployed_model.name)
