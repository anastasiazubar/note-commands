from googleapiclient import discovery
from google.oauth2 import service_account

# Set up credentials and service
credentials = service_account.Credentials.from_service_account_file(
    "your-service-account.json"
)
compute = discovery.build("compute", "v1", credentials=credentials)

project = "your-gcp-project-id"
ssl_policy_name = "tls12-policy"

# Create the SSL policy with min TLS 1.2
ssl_policy_body = {
    "name": ssl_policy_name,
    "minTlsVersion": "TLS_1_2",
    "profile": "MODERN"
}

request = compute.sslPolicies().insert(project=project, body=ssl_policy_body)
response = request.execute()

print("SSL Policy creation started:", response)






##--------




target_https_proxy = "your-https-proxy-name"

update_req = compute.targetHttpsProxies().setSslPolicy(
    project=project,
    targetHttpsProxy=target_https_proxy,
    body={"sslPolicy": f"projects/{project}/global/sslPolicies/{ssl_policy_name}"}
)

update_resp = update_req.execute()
print("SSL Policy applied to target HTTPS proxy:", update_resp)
