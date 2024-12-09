from google.cloud import compute_v1

def add_firewall_policy_association_no_wait(project_id, firewall_policy_id, target, association_name):
    """
    Add an association to a compute firewall policy in GCP without waiting for operation to complete.

    Args:
        project_id: GCP project ID.
        firewall_policy_id: The ID of the firewall policy to which you want to add an association.
        target: The target (e.g., network) for the association.
        association_name: The name for the association.
    """
    client = compute_v1.FirewallPoliciesClient()

    # Create the Firewall Policy Association object
    association = compute_v1.FirewallPolicyAssociation(
        attachment_target=target,
        name=association_name
    )

    # Add the association to the firewall policy
    response = client.add_association(
        firewall_policy=firewall_policy_id,
        firewall_policy_association_resource=association,
        project=project_id
    )

    # The response contains the operation metadata
    print("Association request submitted. Operation details:")
    print(response)

# Example usage
project_id = "your-project-id"
firewall_policy_id = "your-firewall-policy-id"
target = "https://www.googleapis.com/compute/v1/projects/your-project-id/global/networks/your-network-name"
association_name = "example-association"

add_firewall_policy_association_no_wait(project_id, firewall_policy_id, target, association_name)
