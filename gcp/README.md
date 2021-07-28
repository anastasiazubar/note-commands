# note-commands

# Login to GCP via terminal
gcloud auth login
gcloud auth login --no-launch-browser
gcloud config set project PROJECT_ID

# Describe labelson cluster: 
gcloud container clusters describe  cluster-name  --region us-east4 --format "value(resourceLabels)"

# Login to bifrost(VM) from local
gcloud beta compute ssh --internal-ip bifrost-name(vm_name) --project project-name --zone us-east4-a

# Login to Node from cluster, where username -> run whoami. Project need to be set accordingly 
gcloud beta compute ssh --internal-ip username@node-name

# Bucket backup 
gsutil ls
gsutil cp gs://project-name/terraform/state/bucket-name/default.tfstate gs://project-name/terraform/state/bucket-name/default.tfstate_backup


