from google.cloud import pubsub_v1

def update_subscription(project_id, subscription_path, new_ack_deadline_seconds):
    # Create a Pub/Sub client
    subscriber = pubsub_v1.SubscriberClient()

    # Update the ack deadline for the subscription
    subscription = pubsub_v1.types.Subscription(
        name=subscription_path,
        ack_deadline_seconds=new_ack_deadline_seconds
    )

    # Update the subscription
    updated_subscription = subscriber.update_subscription(subscription)

    print(f"Subscription {subscription_path} updated with ack deadline: {new_ack_deadline_seconds} seconds")

# Replace these with your own values
project_id = "your-project-id"
subscription_path = "projects/your-project-id/subscriptions/your-subscription-id"
new_ack_deadline_seconds = 30  # Replace with the new ack deadline value

update_subscription(project_id, subscription_path, new_ack_deadline_seconds)
