from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "FBP API is live!"
