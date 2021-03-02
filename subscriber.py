from google.cloud import pubsub_v1


def subscribe_message():

    subscriber = pubsub_v1.SubscriberClient.from_service_account_json('My First Project-48ecffa9bdef.json')
    timeout = 5.0
    subscription_path = "projects/valid-chess-295400/subscriptions/morse_message-sub"
    
    res = []
    
    def callback(message):
        temp = message.data.decode("utf-8")
        res.append(temp)
        message.ack()

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    #print(f"Listening for messages on {subscription_path}..\n")


    # Wrap subscriber in a 'with' block to automatically call close() when done.
    with subscriber:
        try:
            streaming_pull_future.result(timeout=timeout)
        except:
            streaming_pull_future.cancel()

    #print('Finished Listening for Now.')
    return res