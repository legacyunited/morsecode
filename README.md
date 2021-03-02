# Project Morse Code
Morse Code Transmitter

1. website.py renders the index.html in the templates folder, and the images in the static folder.
2. website.py calls the publisher.py when user inputs message.
3. publisher.py publishes the message to Google Cloud Pub/Sub.
4. listen.py calls subscriber.py which receives the messages from Google Cloud Pub/Sub.
5. listen.py sends the messages to morse.py.
6. morse.py encodes the messages and sends to connected hardware (sg90 mirco servo).

![morse_arch](https://user-images.githubusercontent.com/19507752/109587791-adf3f080-7ad5-11eb-84a1-8e9847550f6c.png)
