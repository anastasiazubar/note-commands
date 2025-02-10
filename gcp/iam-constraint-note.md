Key Differences:
Scope:

managed.iam.managed.disableServiceAccountKeyUpload applies only to managed service accounts (those controlled by Google Cloud services).
boolean.iam.disableServiceAccountKeyUpload applies to all service accounts, including those created by users.
Use Case:

If you want to only restrict key uploads for Google-managed service accounts but allow key uploads for user-created service accounts, use managed.iam.managed.disableServiceAccountKeyUpload.
If you want to completely prevent key uploads for all service accounts, use boolean.iam.disableServiceAccountKeyUpload.
Which One to Use?
If your organization wants a strict security policy that prohibits all service account key uploads, use boolean.iam.disableServiceAccountKeyUpload.
If your organization only wants to limit key uploads for Google-managed service accounts while allowing user-created service accounts to upload keys, use managed.iam.managed.disableServiceAccountKeyUpload.