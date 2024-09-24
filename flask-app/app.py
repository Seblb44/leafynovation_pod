from flask import Flask, jsonify
import paho.mqtt.client as mqtt

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Leafynovation control panel!"})

# You can add more routes and functions here for controlling actuators, fetching data, etc.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

