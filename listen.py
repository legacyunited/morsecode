import subscriber, time, morse
try:
    while True:
        messages = subscriber.subscribe_message()
        
        if len(messages):
            print(f'{len(messages)} message(s)received.')
            
            for each in messages:
                print(each)
                print("Starting transmission of morse code.")
                morse.convert(each.lower())
                print("Completed transmission of morse code.")
                print("Goodbye.")

            messages = []
                    
            
        else:
            print("No message.")

        time.sleep(10)
except KeyboardInterrupt:
    pass

