from google.api_core.exceptions import GoogleAPIError
from google.cloud import functions_v1

def create_cloud_function_with_vpc(project_id, location, function_name, vpc_connector):
    violation_details = []  # To store violation details

    # Create a Cloud Functions client
    client = functions_v1.CloudFunctionsServiceClient()

    # Construct the Cloud Function name
    function_full_name = f"projects/{project_id}/locations/{location}/functions/{function_name}"

    # Define the Cloud Function details including VPC settings
    function = {
        "name": function_full_name,
        "entry_point": "hello_http",  # Replace with your Python function entry point
        "runtime": "python38",  # Python runtime version
        "https_trigger": {},  # HTTP-triggered function
        "vpc_connector": vpc_connector,  # Replace with your VPC connector name
        "vpc_connector_egress_settings": "PRIVATE_RANGES_ONLY",  # VPC Connector egress settings
        # Replace with your function's source code ZIP in a GCS bucket
        "source_archive_url": "gs://cloud-functions-source-code/function_source.zip",
    }

    try:
        # Create the Cloud Function
        response = client.create_function(location=f"projects/{project_id}/locations/{location}", function=function)
        print(f"Cloud Function '{function_name}' created: {response}")

    except GoogleAPIError as e:
        # Handle Google API errors
        errors = getattr(e, "errors", None)
        if errors:
            for error in errors:
                if isinstance(error, dict) and error.get("violations"):
                    for violation in error["violations"]:
                        if violation.get("type") == "constraints/cloudfunctions.requireVPCConnector":
                            violation_details.append({
                                "type": violation.get("type"),
                                "subject": violation.get("subject"),
                                "description": violation.get("description")
                            })
                else:
                    print(f"Other Google API Error: {error}")
                    # Handle other types of errors if needed
        else:
            print(f"Google API Error: {e}")
            # Handle other API errors if needed
    except Exception as general_exception:
        # Handle other general exceptions
        print(f"General Exception: {general_exception}")
        # Add additional error handling or logging here if needed

    return violation_details  # Return the violation details

# Example usage:
project_id = 'YOUR_PROJECT_ID'
location = 'us-central1'
function_name = 'YOUR_FUNCTION_NAME'
vpc_connector_name = 'your-vpc-connector-name'

violations = create_cloud_function_with_vpc(project_id, location, function_name, vpc_connector_name)
if violations:
    print("Violations detected:")
    for violation in violations:
        print(f"Type: {violation['type']}")
        print(f"Subject: {violation['subject']}")
        print(f"Description: {violation['description']}")
