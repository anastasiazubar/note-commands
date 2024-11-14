from google.cloud import compute_v1

def create_instance_with_ipv6(project_id, zone, instance_name, network_name):
    instance_client = compute_v1.InstancesClient()
    network_client = compute_v1.NetworksClient()

    # Step 1: Prepare the network configuration with IPv6
    network = network_client.get(project=project_id, network=network_name)
    access_config = compute_v1.AccessConfig(
        name="External NAT",
        type_=compute_v1.AccessConfig.Type.ONE_TO_ONE_NAT,
        network_tier="PREMIUM"
    )

    # Step 2: Configure the network interface with IPv6
    ipv6_access_config = compute_v1.AccessConfig(
        name="External IPv6",
        type_=compute_v1.AccessConfig.Type.DIRECT_IPV6,
        network_tier="PREMIUM"
    )
    network_interface = compute_v1.NetworkInterface(
        network=network.self_link,
        access_configs=[access_config, ipv6_access_config]
    )

    # Step 3: Define the VM instance settings
    instance = compute_v1.Instance(
        name=instance_name,
        machine_type=f"zones/{zone}/machineTypes/e2-micro",
        network_interfaces=[network_interface],
        disks=[
            compute_v1.AttachedDisk(
                auto_delete=True,
                boot=True,
                initialize_params=compute_v1.AttachedDiskInitializeParams(
                    source_image="projects/debian-cloud/global/images/family/debian-11"
                )
            )
        ]
    )

    # Step 4: Insert (create) the instance
    operation = instance_client.insert(
        project=project_id,
        zone=zone,
        instance_resource=instance
    )
    print(f"Instance creation started: {operation.name}")
    operation.result()  # Waits for the operation to complete
    print(f"Instance created with IPv6 address: {instance_name}")

# Usage example
create_instance_with_ipv6(
    project_id="your-project-id",
    zone="us-central1-a",
    instance_name="my-ipv6-instance",
    network_name="default"  # Use the default network or specify your own
