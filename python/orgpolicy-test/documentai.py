from googleapiclient.discovery import build
from google.oauth2 import service_account

def create_processor_discovery(project_id, location, display_name, processor_type):
    # Load credentials
    credentials = service_account.Credentials.from_service_account_file(
        'path/to/your/service-account.json',
        scopes=['https://www.googleapis.com/auth/cloud-platform']
    )

    # Build the discovery service
    service = build('documentai', 'v1', credentials=credentials)

    parent = f'projects/{project_id}/locations/{location}'

    request_body = {
        "displayName": display_name,
        "type": processor_type
    }

    request = service.projects().locations().processors().create(
        parent=parent,
        body=request_body
    )

    response = request.execute()
    print("Processor created:")
    print(f" - Name: {response['name']}")
    print(f" - Type: {response['type']}")
    print(f" - Display Name: {response['displayName']}")

# Example usage
create_processor_discovery(
    project_id='your-project-id',
    location='us',
    display_name='My OCR Processor',
    processor_type='OCR_PROCESSOR'  # or INVOICE_PROCESSOR, FORM_PARSER_PROCESSOR, etc.
)
