from google.cloud import datastream_v1
from google.protobuf.field_mask_pb2 import FieldMask

def create_public_connection_profile(
    project_id: str,
    location: str,
    connection_profile_id: str,
    display_name: str,
    network: str,
):
    """
    Creates a public connection profile in Google Cloud Datastream.

    :param project_id: GCP project ID.
    :param location: Location of the Datastream service (e.g., "us-central1").
    :param connection_profile_id: The ID for the connection profile.
    :param display_name: A friendly display name for the profile.
    :param network: The name of the VPC network (e.g., "default").
    """

    client = datastream_v1.DatastreamClient()
    parent = f"projects/{project_id}/locations/{location}"

    # Define the connection profile
    connection_profile = datastream_v1.ConnectionProfile(
        display_name=display_name,
        forward_ssh_connectivity=None,  # No SSH tunnel needed for public connection
        gcs_profile=None,  # Not using Google Cloud Storage profile
        private_connectivity=None,  # Public connection, so no private connectivity
        network=network,
    )

    # Create the request
    request = datastream_v1.CreateConnectionProfileRequest(
        parent=parent,
        connection_profile_id=connection_profile_id,
        connection_profile=connection_profile
    )

    # Execute request
    operation = client.create_connection_profile(request=request)
    print("Creating connection profile...")

    # Wait for the operation to complete
    response = operation.result()
    print(f"Connection Profile created: {response.name}")

# Example usage
if __name__ == "__main__":
    create_public_connection_profile(
        project_id="your-project-id",
        location="us-central1",
        connection_profile_id="public-connection-profile",
        display_name="My Public Connection Profile",
        network="default"  # VPC network name
    )