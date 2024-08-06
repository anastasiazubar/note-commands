from google.cloud import dataproc_v1
from google.cloud.dataproc_v1.types import Cluster, ClusterConfig, InstanceGroupConfig, SoftwareConfig
from google.protobuf.duration_pb2 import Duration

def create_cluster(project_id, region, cluster_name):
    cluster_client = dataproc_v1.ClusterControllerClient(client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"})

    # Define the cluster configuration
    cluster = Cluster(
        project_id=project_id,
        cluster_name=cluster_name,
        config=ClusterConfig(
            master_config=InstanceGroupConfig(
                num_instances=1,
                machine_type_uri="n1-standard-2",
                disk_config={"boot_disk_type": "pd-standard", "boot_disk_size_gb": 50},
            ),
            worker_config=InstanceGroupConfig(
                num_instances=2,
                machine_type_uri="n1-standard-2",
                disk_config={"boot_disk_type": "pd-standard", "boot_disk_size_gb": 50},
            ),
            software_config=SoftwareConfig(image_version="1.5-debian10"),
            lifecycle_config=dataproc_v1.LifecycleConfig(
                idle_delete_ttl=Duration(seconds=3600)  # Cluster will be deleted after 1 hour of inactivity
            ),
        ),
    )

    operation = cluster_client.create_cluster(
        request={"project_id": project_id, "region": region, "cluster": cluster}
    )

    print(f"Creating cluster {cluster_name}...")
    result = operation.result()
    print(f"Cluster created successfully: {result.cluster_name}")

# Replace with your project ID, region, and desired cluster name
project_id = "your-project-id"
region = "your-region"  # e.g., "us-central1"
cluster_name = "your-cluster-name"

create_cluster(project_id, region, cluster_name)
