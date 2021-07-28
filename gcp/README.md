# note-commands

# Login to GCP via terminal
gcloud auth login
gcloud auth login --no-launch-browser
gcloud config set project PROJECT_ID

# Describe labelson cluster: 
gcloud container clusters describe  carbon-admin-us-east4-diamond  --region us-east4 --format "value(resourceLabels)"

# Login to bifrost(VM) from local
gcloud beta compute ssh --internal-ip bifrost-us-east4-a --project gcp-ushi-carbon-predevops-npe --zone us-east4-a

# Login to Node from cluster, where c3570714 -> username. Project need to be set accordingly 
gcloud beta compute ssh --internal-ip c3570714@node-name

