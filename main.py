from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

DATA_FILE = "trades.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        trades = json.load(file)
else:
    trades = []

@app.route("/")
def home():
    return "FBP API is live!"

@app.route("/trades", methods=["GET"])
def get_trades():
    return jsonify(trades)

@app.route("/trades", methods=["POST"])
def submit_trade():
    trade = request.json
    if "teamA" not in trade or "teamB" not in trade or "players" not in trade:
        return jsonify({"error": "Invalid trade format"}), 400

    trades.append(trade)
    with open(DATA_FILE, "w") as file:
        json.dump(trades, file, indent=4)

    return jsonify({"message": "Trade successfully submitted!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
