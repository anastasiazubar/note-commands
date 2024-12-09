from google.cloud import compute_v1
from google.oauth2 import service_account

# Set up credentials
credentials = service_account.Credentials.from_service_account_file(
    'path/to/your/service-account-file.json'
)

# Set up compute client
compute_client = compute_v1.FirewallPoliciesClient(credentials=credentials)

# Define the firewall policy and network
project_id = 'your-project-id'
firewall_policy_id = 'your-firewall-policy-id'
region = 'your-region'  # or 'global' for global scope
network = 'projects/your-project-id/global/networks/your-vpc-network'

# Build the association request
request = compute_v1.AddAssociationFirewallPolicyRequest(
    firewall_policy=firewall_policy_id,
    network=network,
    project=project_id,
)

# Add the association
operation = compute_client.add_association(request=request)

# Wait for the operation to complete (optional)
operation.result()  # This blocks until the operation is finished

print(f"Firewall policy {firewall_policy_id} successfully associated with network {network}")
