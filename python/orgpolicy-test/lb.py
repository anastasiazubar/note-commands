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
