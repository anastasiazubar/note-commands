from googleapiclient.discovery import build
from google.oauth2 import service_account

# Set up credentials
credentials = service_account.Credentials.from_service_account_file(
    'path/to/your/service-account-file.json'
)

# Initialize the Compute Engine API client
compute = build('compute', 'v1', credentials=credentials)

# Define the parameters
project = 'prj-iam-denytest'  # Your project ID
firewall_policy = '6881911111241'  # Firewall policy ID
network = 'projects/prj-iam-denytest/global/networks/tf-test'  # VPC network path

# Define the association object
association = {
    'attachmentTarget': network  # The target to attach the firewall policy to
}

# Add the association
request = compute.firewallPolicies().addAssociation(
    project=project,
    firewallPolicy=firewall_policy,
    body=association
)

# Execute the request and handle the response
response = request.execute()

# Print the response to see the result
print(response)
