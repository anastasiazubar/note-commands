from google.cloud import kms_v1
from google.protobuf import duration_pb2

def create_key_ring_and_key(project_id, location_id, key_ring_id, crypto_key_id):
    # Initialize the KMS client
    client = kms_v1.KeyManagementServiceClient()

    # Construct the location path
    location_path = client.common_location_path(project_id, location_id)

    # Create the KeyRing
    key_ring_path = f"{location_path}/keyRings/{key_ring_id}"
    try:
        key_ring = client.create_key_ring(
            request={"parent": location_path, "key_ring_id": key_ring_id, "key_ring": {}}
        )
        print(f"Created KeyRing: {key_ring.name}")
    except Exception as e:
        print(f"Error creating KeyRing: {e}")
        return

    # Define the CryptoKey settings
    key_purpose = kms_v1.enums.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT
    key = {
        "purpose": key_purpose,
        "version_template": {"algorithm": kms_v1.enums.CryptoKeyVersion.CryptoKeyVersionAlgorithm.GOOGLE_SYMMETRIC_ENCRYPTION},
        "rotation_period": duration_pb2.Duration(seconds=60 * 60 * 24 * 365),  # 1 year
    }

    # Create the CryptoKey
    try:
        crypto_key = client.create_crypto_key(
            request={
                "parent": key_ring_path,
                "crypto_key_id": crypto_key_id,
                "crypto_key": key,
            }
        )
        print(f"Created CryptoKey: {crypto_key.name}")
    except Exception as e:
        print(f"Error creating CryptoKey: {e}")

# Replace with your project details
project_id = "your-project-id"
location_id = "us-central1"  # Replace with your GCP region
key_ring_id = "my-key-ring"
crypto_key_id = "my-crypto-key"

create_key_ring_and_key(project_id, location_id, key_ring_id, crypto_key_id)
