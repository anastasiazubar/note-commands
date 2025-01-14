try:
    # Parse the JSON content
    error_details = json.loads(response_content)
    
    # Extract the message field
    error_message = error_details.get("error", {}).get("message", "No error message found")
    
    # Raise exception with the specific message
    raise Exception(f"Exception happened: {error_message}")