from google.cloud import dns
from google.protobuf.duration_pb2 import Duration

def create_dns_policy(project_id, policy_name, alternative_dns_servers):
    client = dns.Client()

    # Prepare the DNS policy request
    policy = client.policy(policy_name)
    policy.alternative_name_server_configs = alternative_dns_servers

    # Create the DNS policy
    operation = policy.create()
    operation.wait_for_completion(timeout=Duration(seconds=30))

    print(f"DNS policy '{policy_name}' created successfully.")

# Provide your project ID, policy name, and alternative DNS servers
project_id = "your-project-id"
policy_name = "your-policy-name"
alternative_dns_servers = [
    dns.PolicyAlternativeNameServerConfig(
        target_name_server=dns.TargetNameServer(
            ipv4_address="8.8.8.8"
        ),
        forwarding_zone_name="example.com."
    ),
    dns.PolicyAlternativeNameServerConfig(
        target_name_server=dns.TargetNameServer(
            ipv4_address="8.8.4.4"
        ),
        forwarding_zone_name="example.net."
    )
]

create_dns_policy(project_id, policy_name, alternative_dns_servers)
