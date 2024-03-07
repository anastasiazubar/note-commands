from google.cloud import bigquery
from google.cloud import kms_v1

# Set your GCP project ID and location
project_id = 'your-project-id'
location = 'US'  # Change to your desired location

# Initialize BigQuery and KMS clients
bigquery_client = bigquery.Client(project=project_id)
kms_client = kms_v1.KeyManagementServiceClient()

# Create the dataset
dataset_id = 'your_dataset_id'
dataset_ref = bigquery_client.dataset(dataset_id)

# Optionally, specify the default encryption configuration for the dataset
# If not specified, BigQuery will use Google-managed encryption
encryption_config = bigquery.EncryptionConfiguration(
    kms_key_name='projects/{}/locations/{}/keyRings/{}/cryptoKeys/{}'.format(
        project_id, location, 'your-keyring', 'your-kms-key'
    )
)

dataset = bigquery.Dataset(dataset_ref)
dataset.location = location
dataset.default_encryption_configuration = encryption_config

try:
    bigquery_client.create_dataset(dataset)
    print(f"Dataset {dataset_id} created.")
except Exception as e:
    print(f"Error creating dataset: {e}")

# If you haven't created a KMS key yet, you can create one using KMS client
# If you already have a KMS key, you need to get its resource ID
# For example:
# key_id = 'projects/{}/locations/{}/keyRings/{}/cryptoKeys/{}'.format(
#     project_id, location, 'your-keyring', 'your-kms-key'
# )





############




from google.cloud import bigquery
from google.cloud import kms_v1

def create_dataset_with_kms(project_id, dataset_id, location, kms_key_resource_id):
    """Creates a BigQuery dataset with encryption using a Customer-Managed Encryption Key."""
    # Initialize BigQuery client
    bigquery_client = bigquery.Client(project=project_id)

    # Initialize KMS client
    kms_client = kms_v1.KeyManagementServiceClient()

    # Create the dataset
    dataset_ref = bigquery_client.dataset(dataset_id)
    dataset = bigquery.Dataset(dataset_ref)
    dataset.location = location

    # Specify the encryption configuration
    encryption_config = bigquery.EncryptionConfiguration(
        kms_key_name=kms_key_resource_id
    )
    dataset.default_encryption_configuration = encryption_config

    try:
        bigquery_client.create_dataset(dataset)
        print(f"Dataset {dataset_id} created with encryption using KMS key {kms_key_resource_id}.")
    except Exception as e:
        print(f"Error creating dataset: {e}")

# Example usage:
project_id = 'your-project-id'
dataset_id = 'your-dataset-id'
location = 'US'
kms_key_resource_id = 'projects/your-project-id/locations/global/keyRings/your-key-ring/cryptoKeys/your-key'

create_dataset_with_kms(project_id, dataset_id, location, kms_key_resource_id)
