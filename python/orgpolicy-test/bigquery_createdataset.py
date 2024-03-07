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
