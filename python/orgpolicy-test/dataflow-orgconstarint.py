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
