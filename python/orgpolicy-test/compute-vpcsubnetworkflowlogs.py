from google.cloud import compute_v1
from google.oauth2 import service_account

# Set your project, region, and subnet details
project_id = 'your-project-id'
region = 'your-region'
subnet_name = 'your-subnet-name'

# Set up your credentials (use your service account key file)
credentials = service_account.Credentials.from_service_account_file(
    'path/to/your/service-account-key.json'
)

# Create the Compute Engine client
client = compute_v1.SubnetworksClient(credentials=credentials)

# Define the VPC Flow Logs settings
subnet = client.get(project=project_id, region=region, subnetwork=subnet_name)

# Modify the flow logs to "ESSENTIAL" level (this configures basic logging)
subnet.enable_flow_logs = True
subnet.flow_logs_sampling = 1.0  # Set the sample rate (1.0 means log every flow)
subnet.flow_logs_aggregation_interval = "INTERVAL_5_SEC"  # Optional interval for aggregation

# Send the request to update the subnet
operation = client.update(
    project=project_id, 
    region=region, 
    subnetwork=subnet_name, 
    subnetwork_resource=subnet
)

# Wait for the operation to complete
operation.result()

print(f"Flow logs have been enabled for subnet {subnet_name} in region {region}.")
