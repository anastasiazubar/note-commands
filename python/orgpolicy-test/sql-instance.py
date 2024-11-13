from google.cloud import sqladmin_v1
from google.oauth2 import service_account

# Set up credentials and the SQL Admin client
credentials = service_account.Credentials.from_service_account_file(
    'path_to_your_service_account_key.json'
)
sqladmin_client = sqladmin_v1.SqlInstancesServiceClient(credentials=credentials)

# Define instance configuration
instance_body = {
    "name": "your-instance-name",
    "database_version": "POSTGRES_13",  # Use appropriate database version (POSTGRES_13, MYSQL_8_0, etc.)
    "settings": {
        "tier": "db-f1-micro",  # Use an appropriate machine type
        "ip_configuration": {
            "ipv4_enabled": True,  # Enable public IP
        },
        # Additional configurations like backup, storage, and replication
    },
    "region": "us-central1",  # Specify the region
}

# Create the instance
project_id = "your-project-id"
request = sqladmin_v1.CreateInstanceRequest(parent=f"projects/{project_id}", body=instance_body)

try:
    operation = sqladmin_client.insert(request=request)
    print(f"Instance creation initiated: {operation.name}")
except Exception as e:
    print(f"An error occurred: {e}")
