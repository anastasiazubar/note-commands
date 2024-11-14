from google.cloud import compute_v1

def create_simple_instance_with_ipv6_and_cmek(project_id, zone, instance_name, kms_key):
    instance_client = compute_v1.InstancesClient()

    # Define network interface with basic IPv6 config
    network_interface = compute_v1.NetworkInterface(
        access_configs=[
            # Standard IPv4 Access
            compute_v1.AccessConfig(
                name="External NAT",
                type_=compute_v1.AccessConfig.Type.ONE_TO_ONE_NAT
            ),
            # IPv6 Access
            compute_v1.AccessConfig(
                name="External IPv6",
                type_=compute_v1.AccessConfig.Type.DIRECT_IPV6
            )
        ]
    )

    # Define a boot disk with CMEK
    disk = compute_v1.AttachedDisk(
        auto_delete=True,
        boot=True,
        initialize_params=compute_v1.AttachedDiskInitializeParams(
            source_image="projects/debian-cloud/global/images/family/debian-11",
            disk_encryption_key=compute_v1.CustomerEncryptionKey(
                kms_key_name=kms_key
            )
        )
    )

    # Define a minimal VM instance
    instance = compute_v1.Instance(
        name=instance_name,
        machine_type=f"zones/{zone}/machineTypes/e2-micro",
        network_interfaces=[network_interface],
        disks=[disk]
    )

    # Create the instance
    operation = instance_client.insert(
        project=project_id,
        zone=zone,
        instance_resource=instance
    )
    print(f"Instance creation started: {operation.name}")
    operation.result()  # Wait for the operation to complete
    print(f"Instance created with IPv6 and CMEK: {instance_name}")

# Usage example
create_simple_instance_with_ipv6_and_cmek(
    project_id="your-project-id",
    zone="us-central1-a",
    instance_name="ipv6-cmek-test-instance",
    kms_key="projects/your-project-id/locations/global/keyRings/my-key-ring/cryptoKeys/my-cmek-key"
)
