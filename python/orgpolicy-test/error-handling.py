    except requests.exceptions.HTTPError as http_err:
        LOGGER.error(f"HTTP error occurred: {http_err}")
        return {
            "error": "HTTPError",
            "status_code": response.status_code,
            "content": response.content.decode("utf-8")
        }

    except requests.exceptions.RequestException as req_err:
        LOGGER.error(f"Request error occurred: {req_err}")
        return {
            "error": "RequestException",
            "message": str(req_err)
        }