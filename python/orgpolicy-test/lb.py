from googleapiclient.discovery import build

def create_https_lb_with_tls(project_id):
    compute = build("compute", "v1")

    # 1. Create Load Balancer (HTTPS) with TLS 1.1 in a single step
    lb_body = {
        "name": "https-load-balancer",
        "target": {
            "name": "https-target-proxy",
            "urlMap": f"projects/{project_id}/global/urlMaps/default",
            "sslPolicy": {
                "name": "tls-1-1-policy",
                "profile": "MODERN",
                "minTlsVersion": "TLS_1_1"
            },
            "sslCertificates": [f"projects/{project_id}/global/sslCertificates/default"]
        },
        "forwardingRule": {
            "name": "https-forwarding-rule",
            "portRange": "443",
            "loadBalancingScheme": "EXTERNAL"
        }
    }

    compute.globalForwardingRules().insert(
        project=project_id, body=lb_body
    ).execute()

    print(f"HTTPS Load Balancer created with TLS 1.1 in one step!")

# Usage
create_https_lb_with_tls("your-project-id")




Correct IAM Permissions Required
You need these specific permissions to create and configure an HTTPS Load Balancer:

1. Forwarding Rule Permissions
compute.globalForwardingRules.create
compute.globalForwardingRules.get
compute.globalForwardingRules.list
compute.globalForwardingRules.use
2. Target HTTPS Proxy Permissions
compute.targetHttpsProxies.create
compute.targetHttpsProxies.get
compute.targetHttpsProxies.list
compute.targetHttpsProxies.use
3. SSL Policy Permissions (To Specify TLS Version)
compute.sslPolicies.create
compute.sslPolicies.get
compute.sslPolicies.list
compute.sslPolicies.use
4. URL Map Permissions
compute.urlMaps.create
compute.urlMaps.get
compute.urlMaps.list
compute.urlMaps.use
5. SSL Certificate Permissions
compute.sslCertificates.create
compute.sslCertificates.get
compute.sslCertificates.list
compute.sslCertificates.use
6. Backend Service Permissions
compute.backendServices.create
compute.backendServices.get
compute.backendServices.list
compute.backendServices.use
