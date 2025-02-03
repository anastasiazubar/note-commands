from google.cloud import compute_v1

def create_vpc_peering(project_id, network1, network2):
    client = compute_v1.NetworksClient()

    peer_request1 = compute_v1.NetworksAddPeeringRequest(
        network_peering=compute_v1.NetworkPeering(
            name=f"{network1}-to-{network2}",
            network=f"projects/{project_id}/global/networks/{network2}",
            exchange_subnet_routes=True
        )
    )

    peer_request2 = compute_v1.NetworksAddPeeringRequest(
        network_peering=compute_v1.NetworkPeering(
            name=f"{network2}-to-{network1}",
            network=f"projects/{project_id}/global/networks/{network1}",
            exchange_subnet_routes=True
        )
    )

    # Add peering to network1
    operation1 = client.add_peering(project=project_id, network=network1, networks_add_peering_request_resource=peer_request1)
    print(f"Peering {network1} -> {network2} initiated: {operation1.name}")

    # Add peering to network2
    operation2 = client.add_peering(project=project_id, network=network2, networks_add_peering_request_resource=peer_request2)
    print(f"Peering {network2} -> {network1} initiated: {operation2.name}")

# Example Usage
create_vpc_peering("your-project-id", "network-1", "network-2")