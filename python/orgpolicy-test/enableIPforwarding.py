from googleapiclient import discovery
from google.auth import default

project = 'your-project-id'
zone = 'your-zone'
instance_name = 'your-instance-name'
machine_type = f"zones/{zone}/machineTypes/e2-medium"
source_image = "projects/debian-cloud/global/images/family/debian-11"
network = "global/networks/default"

credentials, _ = default()
compute = discovery.build('compute', 'v1', credentials=credentials)

config = {
    "name": instance_name,
    "machineType": machine_type,
    "canIpForward": True,  # ✅ Enable IP forwarding
    "disks": [{
        "boot": True,
        "autoDelete": True,
        "initializeParams": {
            "sourceImage": source_image
        }
    }],
    "networkInterfaces": [{
        "network": network,
        "accessConfigs": [{
            "type": "ONE_TO_ONE_NAT",
            "name": "External NAT"
        }]
    }]
}

operation = compute.instances().insert(
    project=project,
    zone=zone,
    body=config
).execute()

print(f"Created VM with IP forwarding enabled. Operation ID: {operation['name']}")





region = 'us-east4'  # or the region where your subnet exists
subnet_name = 'your-subnet-name'
subnet_link = f"projects/{project}/regions/{region}/subnetworks/{subnet_name}"

config = {
    "name": instance_name,
    "machineType": machine_type,
    "canIpForward": True,
    "disks": [{
        "boot": True,
        "autoDelete": True,
        "initializeParams": {
            "sourceImage": source_image
        }
    }],
    "networkInterfaces": [{
        "network": f"projects/{project}/global/networks/{network_name}",
        "subnetwork": subnet_link,  # ✅ required for custom VPCs
        "accessConfigs": [{
            "type": "ONE_TO_ONE_NAT",
            "name": "External NAT"
        }]
    }]
}
