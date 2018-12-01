#!/bin/pyhton3.6
import os,sys
from flask import Flask,request
from pymessenger import Bot
app = Flask(__name__)



# Set GROOT_TOKEN to Access Token from your APP on Developers.facebook

GROOT_TOKEN = ""
GROOT = Bot(GROOT_TOKEN)

@app.route('/' , methods=['GET'])

def verify():
    # Webhook
    if request.args.get('hub.mode') == 'subscribe':
        if not request.args.get('hub.verify_token') == "Groot" :
            return "Verification token mismatch" , 403
        return request.args["hub.challenge"], 200
    return "Hello: I am GROOT :D" , 200



@app.route('/' , methods=['POST'])
def webhook ():
    data = request.get_json()
    log(data)
    for entry in data['entry']:
        for mess in entry['messaging']:

            SENDER_ID = mess['sender']['id']
            RECIPIENT_ID = mess['recipient']['id']

            if mess.get('message'):
                if 'text' in mess['message'] :
                    recv = mess['message']['text']
                else :
                    recv = "No Text :("
                # REPLAY
                replay = "I AM GROOT"
                if recv.lower() == "we will shut you down":
                    replay = "WE ARE GROOT"
                GROOT.send_text_message(SENDER_ID , replay)

    return 'ok' , 200

def log (message):
    print (message)
    sys.stdout.flush()

if __name__ == "__main__":
    app.run(debug=True , port = 80)


