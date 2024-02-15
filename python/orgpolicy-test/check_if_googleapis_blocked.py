import requests

def main():
    url = "https://domains.googleapis.com/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("domains.googleapis.com is accessible.")
        else:
            print(f"Request to domains.googleapis.com failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while accessing domains.googleapis.com: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
