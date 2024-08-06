from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

# Project and job settings
project_id = 'your-project-id'
gcs_temp_location = 'gs://your-temp-bucket/temp/'
gcs_staging_location = 'gs://your-temp-bucket/staging/'
job_name = 'your-job-name'

# Create a Dataflow client
dataflow = build('dataflow', 'v1b3')

# Define the job
job = {
    "jobName": job_name,
    "environment": {
        "tempLocation": gcs_temp_location,
        "stagingLocation": gcs_staging_location,
        "zone": "us-central1-f"
    },
    "steps": [
        {
            "name": "Read from Text",
            "properties": {
                "inputFile": "gs://your-input-bucket/input.txt",
                "outputFile": "gs://your-output-bucket/output.txt",
                "type": "Read"
            }
        },
        {
            "name": "Write to Text",
            "properties": {
                "type": "Write"
            }
        }
    ]
}

try:
    # Submit the job to Dataflow
    request = dataflow.projects().locations().jobs().create(
        projectId=project_id,
        location='us-central1',
        body=job
    )
    response = request.execute()
    print('Job created successfully: {}'.format(json.dumps(response, indent=2)))
except HttpError as err:
    print('Error occurred: {}'.format(err))




################


from google.cloud import dataflow_v1beta3
from google.protobuf import duration_pb2

# Define your project and job settings
project_id = 'your-project-id'
job_name = 'your-job-name'
temp_location = 'gs://your-temp-bucket/temp/'
gcs_staging_location = 'gs://your-staging-bucket/staging/'
region = 'us-central1'

# Initialize the Dataflow client
client = dataflow_v1beta3.JobsV1Beta3Client()

# Define the job parameters
job = dataflow_v1beta3.Job(
    name=job_name,
    type=dataflow_v1beta3.JobType.JOB_TYPE_STREAMING,
    environment=dataflow_v1beta3.Environment(
        temp_location=temp_location,
        staging_location=gcs_staging_location,
        zone='us-central1-f',
    ),
    steps=[
        {
            "name": "Read from Text",
            "properties": {
                "inputFile": "gs://your-input-bucket/input.txt",
                "outputFile": "gs://your-output-bucket/output.txt",
                "type": "Read"
            }
        },
        {
            "name": "Write to Text",
            "properties": {
                "type": "Write"
            }
        }
    ]
)

# Set the job creation request
create_request = dataflow_v1beta3.CreateJobRequest(
    project_id=project_id,
    location=region,
    job=job,
)

# Submit the job
response = client.create_job(request=create_request)

print(f"Job created successfully: {response.name}")
