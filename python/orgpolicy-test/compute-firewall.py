from google.cloud import compute_v1

def add_firewall_policy_association(project_id, firewall_policy_id, region, target, association_name):
    """
    Add an association to a compute firewall policy in GCP.

    Args:
        project_id: GCP project ID.
        firewall_policy_id: The ID of the firewall policy to which you want to add an association.
        region: The region of the target resource.
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
    operation = client.add_association(
        firewall_policy=firewall_policy_id,
        firewall_policy_association_resource=association,
        region=region,
        project=project_id
    )

    # Wait for the operation to complete
    print("Adding association to the firewall policy...")
    operation_client = compute_v1.GlobalOperationsClient()
    operation = operation_client.wait(project=project_id, operation=operation.name)
    if operation.status == compute_v1.Operation.Status.DONE:
        print("Association added successfully!")
    else:
        print("Failed to add the association.")

# Example usage
project_id = "your-project-id"
firewall_policy_id = "your-firewall-policy-id"
region = "your-region"
target = "target-network-or-resource"
association_name = "example-association"

add_firewall_policy_association(project_id, firewall_policy_id, region, target, association_name)
