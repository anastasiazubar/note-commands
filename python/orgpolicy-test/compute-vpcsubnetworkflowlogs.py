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


-----------


from google.cloud import compute_v1
from google.oauth2 import service_account

# Set your project, region, VPC network, and subnet details
project_id = 'your-project-id'
region = 'your-region'
vpc_network_name = 'your-vpc-network-name'
subnet_name = 'new-subnet-name'

# Set up your credentials (use your service account key file)
credentials = service_account.Credentials.from_service_account_file(
    'path/to/your/service-account-key.json'
)

# Define the Compute Engine client
client = compute_v1.SubnetworksClient(credentials=credentials)

# Define the subnet properties
subnet = compute_v1.Subnetwork(
    name=subnet_name,
    region=region,
    network=f"projects/{project_id}/global/networks/{vpc_network_name}",
    ip_cidr_range="10.0.1.0/24",  # Define the CIDR range for the subnet
    enable_flow_logs=True,
    # Essential flow log settings:
    log_config=compute_v1.SubnetworkLogConfig(
        enable=True,
        aggregation_interval=compute_v1.SubnetworkLogConfig.AggregationInterval.INTERVAL_5_SEC,
        flow_sampling=0.2,  # Sampling rate between 0.1 and 0.5 for ESSENTIAL
        metadata=compute_v1.SubnetworkLogConfig.Metadata.INCLUDE_ALL_METADATA,
    )
)

# Create the subnet
operation = client.insert(
    project=project_id,
    region=region,
    subnetwork_resource=subnet
)

# Wait for the operation to complete
operation.result()

print(f"Subnet {subnet_name} created with ESSENTIAL flow logging in VPC {vpc_network_name}.")
