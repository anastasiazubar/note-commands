from google.cloud.devtools import cloudbuild_v1
from google.auth import default

def trigger_cloud_build_with_workerpool(project_id: str, worker_pool: str = "projects/test/locations/global/workerPools/test@test.com"):
    """
    Triggers a simple Cloud Build job using a specific allowed worker pool.
    
    Args:
        project_id (str): GCP Project ID.
        worker_pool (str): Full resource name of the allowed worker pool.
    """
    # Authenticate and create Cloud Build client
    credentials, _ = default()
    client = cloudbuild_v1.CloudBuildClient(credentials=credentials)

    # Define build configuration
    build = {
        "steps": [
            {
                "name": "gcr.io/cloud-builders/gcloud",
                "args": ["version"]
            }
        ],
        "options": {
            "worker_pool": worker_pool
        }
    }

    # Submit build
    operation = client.create_build(project_id=project_id, build=build)
    print("Build triggered. Waiting for completion...")
    result = operation.result()
    print("Build finished with status:", result.status.name)





from googleapiclient import discovery

def submit_build_with_private_pool():
    # Define GCP project and pool details
    PROJECT_ID = "2348848349"        # GCP project ID (or number)
    REGION = "us-central1"           # Region where the worker pool is created
    WORKER_POOL_ID = "my-private-pool"  # Worker pool ID (name) – change to your pool's ID
    
    # Full resource path of the worker pool (required by Cloud Build API)
    workerpool_resource = f"projects/{PROJECT_ID}/locations/{REGION}/workerPools/{WORKER_POOL_ID}"
    
    # Define the build configuration
    build_config = {
        "steps": [ 
            {   # Example build step: print a message
                "name": "alpine", 
                "entrypoint": "/bin/sh", 
                "args": ["-c", "echo 'Hello from private pool'"]
            }
        ],
        # You can include other build fields like 'images', 'artifacts', etc. as needed
        "workerPool": workerpool_resource  # Specify the private worker pool to use
    }
    
    # Initialize Cloud Build API client
    cloudbuild = discovery.build("cloudbuild", "v1")
    # Submit the build to Cloud Build
    request = cloudbuild.projects().builds().create(projectId=PROJECT_ID, body=build_config)
    response = request.execute()
    print(f"Build submitted. Operation: {response['name']}")
