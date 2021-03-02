from google.cloud import pubsub_v1

# -------- publish to topic ----------
project_id = "valid-chess-295400"
topic_id = "morse_message"

publisher = pubsub_v1.PublisherClient.from_service_account_json('My First Project-48ecffa9bdef.json')
topic_path = "projects/valid-chess-295400/topics/morse_message"

def publish_message(message):
    data = f"{message}"
    # Data must be a bytestring
    data = data.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    print(future.result(), f"Published messages to {topic_path}.")