from flask import Flask,render_template,redirect,request,flash
import time
import publisher
 
app = Flask(__name__)
app.secret_key = "something only you know"

 
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/publish', methods=['GET', 'POST'])
def publish():
    message = request.form['text-id'] 
    if len(message):
        publisher.publish_message(message)
        flash('Message Trasmitted')
    else:
        flash('Enter a message')
    return redirect('/')
 
app.run(host='localhost', port=5000, debug=True)