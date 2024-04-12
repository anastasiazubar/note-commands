from google.cloud import aiplatform

# Set your project ID, location, endpoint ID, and model ID
project_id = "your-project-id"
location = "us-central1"
endpoint_id = "your-endpoint-id"
model_id = "your-model-id"

# Initialize the AI Platform client
client_options = {"api_endpoint": f"{location}-aiplatform.googleapis.com"}
client = aiplatform.gapic.EndpointServiceClient(client_options=client_options)

# Define the model name and endpoint name
model_name = f"projects/{project_id}/locations/{location}/models/{model_id}"
endpoint_name = f"projects/{project_id}/locations/{location}/endpoints/{endpoint_id}"

# Set the deployment request
deploy_model_request = aiplatform.gapic.DeployModelRequest(
    endpoint=endpoint_name,
    deployed_model=aiplatform.gapic.DeployedModel(
        id=model_id,
        model=model_name,
        display_name="your-deployed-model-name",
        machine_type="n1-standard-4",
    ),
)

# Deploy the model to the endpoint
response = client.deploy_model(request=deploy_model_request)

# Display deployment information
print("Model deployed to endpoint with ID:", response.deployed_model.id)
