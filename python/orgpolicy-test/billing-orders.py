from google.oauth2 import service_account
from googleapiclient.discovery import build

# Replace with your own service account file path
SERVICE_ACCOUNT_FILE = "path/to/your/service-account-key.json"
SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]

# Replace with your billing account ID
BILLING_ACCOUNT_ID = "billingAccounts/your-billing-account-id"

def place_order():
    # Authenticate and initialize the API client
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("consumerprocurement", "v1alpha1", credentials=credentials)
    
    # Construct the order details
    order_body = {
        "displayName": "My Test Order",
        "lineItems": [
            {
                "lineItemId": "test-item-id",
                "product": "projects/your-project-id/products/your-product-id",
                "quantity": 1,
            }
        ],
    }
    
    # Place the order
    try:
        request = service.billingAccounts().orders().place(
            parent=f"billingAccounts/{BILLING_ACCOUNT_ID}",
            body=order_body
        )
        response = request.execute()
        print("Order placed successfully:")
        print(response)
    except Exception as e:
        print("An error occurred while placing the order:")
        print(e)

if __name__ == "__main__":
    place_order()
