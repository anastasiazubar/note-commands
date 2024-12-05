from google.auth import compute_engine
from googleapiclient import discovery

# Initialize the Compute Engine API client
credentials = compute_engine.Credentials()
service = discovery.build('compute', 'v1', credentials=credentials)

# Specify your project, zone, and instance
project = 'your-project-id'
zone = 'your-zone'
instance = 'your-instance-name'

# Set the serial port to read from (default is 1, but can be adjusted)
serial_port = 1

# Get the serial port output
request = service.instances().getSerialPortOutput(
    project=project,
    zone=zone,
    instance=instance,
    port=serial_port
)

# Execute the request
response = request.execute()

# Print the serial port output
print(response.get('contents', 'No serial output available'))
