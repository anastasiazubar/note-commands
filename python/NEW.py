import googleapiclient.discovery
from google.oauth2 import service_account

def update_iam_policy(bucket_name, object_name, policy):
    # Set the necessary credentials
    credentials = service_account.Credentials.from_service_account_file(
        'path/to/credentials.json'
    )

    # Create a storage service client
    service = googleapiclient.discovery.build('storage', 'v1', credentials=credentials)

    # Construct the resource name for the object
    resource_name = f"projects/_/buckets/{bucket_name}/objects/{object_name}"

    # Construct the request body with the updated policy
    request_body = {
        'policy': policy
    }

    # Update the IAM policy for the object
    response = service.objects().setIamPolicy(
        resource=resource_name,
        body=request_body
    ).execute()

    print(f"IAM policy updated for object {object_name} in bucket {bucket_name}.")

# Usage
bucket_name = 'your-bucket-name'
object_name = 'your-object-name'
policy = {
    'bindings': [
        {
            'role': 'roles/storage.objectViewer',
            'members': ['user:example@example.com']
        },
        {
            'role': 'roles/storage.objectAdmin',
            'members': ['user:admin@example.com']
        }
    ]
}

update_iam_policy(bucket_name, object_name, policy)
