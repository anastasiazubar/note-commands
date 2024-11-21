from google.cloud import compute_v1

def create_instance(project_id, zone, instance_name):
    instance_client = compute_v1.InstancesClient()

    # Define the machine type and boot disk
    machine_type = f"zones/{zone}/machineTypes/e2-medium"
    boot_disk_initialize_params = {
        "source_image": "projects/debian-cloud/global/images/debian-11"
    }
    boot_disk = compute_v1.AttachedDisk(
        auto_delete=True,
        boot=True,
        initialize_params=compute_v1.AttachedDiskInitializeParams(**boot_disk_initialize_params),
    )

    # Local SSD disk (scratch disk)
    scratch_disk = compute_v1.AttachedDisk(
        auto_delete=True,
        type_="SCRATCH",
        interface="SCSI"
    )

    # Network interface configuration
    network_interface = compute_v1.NetworkInterface(
        network="projects/your-project-id/global/networks/default",
        subnetwork="regions/us-east4/subnetworks/your-subnetwork",
        access_configs=[compute_v1.AccessConfig(
            name="External NAT",
            type_="ONE_TO_ONE_NAT"
        )]
    )

    # Metadata
    metadata_items = [
        {"key": "enable-oslogin-2fa", "value": "true"},
        {"key": "enable-oslogin", "value": "true"}
    ]
    metadata = compute_v1.Metadata(items=metadata_items)

    # Construct the instance
    instance = compute_v1.Instance(
        name=instance_name,
        machine_type=machine_type,
        disks=[boot_disk, scratch_disk],
        network_interfaces=[network_interface],
        metadata=metadata,
        tags=compute_v1.Tags(items=["foo", "bar"]),
    )

    # Make the request to create the instance
    operation = instance_client.insert(
        project=project_id,
        zone=zone,
        instance_resource=instance
    )

    print(f"Operation to create instance {instance_name}: {operation.name}")

# Replace with your values
project_id = "your-project-id"
zone = "us-east4-a"
instance_name = "test-default-sa"

create_instance(project_id, zone, instance_name)
