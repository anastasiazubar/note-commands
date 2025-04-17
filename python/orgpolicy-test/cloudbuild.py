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
