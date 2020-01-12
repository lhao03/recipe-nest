# /index.py
from flask import Flask, request, jsonify, render_template
import os
import dialogflow
import requests
import json
import pusher

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)
    allParameters = data['queryResult']['parameters']
    reply = {
        "fulfillmentText": "Ok. Tickets booked successfully.",
    }
    return jsonify(reply)


# run Flask app
if __name__ == "__main__":
    app.run()
