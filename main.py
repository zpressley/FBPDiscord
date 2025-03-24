from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)  # 👈 this enables all origins by default

@app.route("/")
def home():
    return "FBP API is live!"

# Get PORT from environment or use 5000 locally
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
@app.route("/trades", methods=["POST"])
def submit_trade():
    trade = request.json

    # Basic validation
    required_fields = ["teamA", "teamB", "players"]
    if not all(field in trade and trade[field] for field in required_fields):
        return jsonify({"error": "All fields (teamA, teamB, players) are required."}), 400

    if trade["teamA"].strip().lower() == trade["teamB"].strip().lower():
        return jsonify({"error": "Team A and Team B must be different."}), 400

    if len(trade["players"].strip()) < 3:
        return jsonify({"error": "You must specify at least one player involved in the trade."}), 400

    # Future validation example: validate players are in known database
    # known_players = load_player_list()
    # if not all(p in known_players for p in extract_players(trade["players"])):
    #     return jsonify({"error": "One or more players not found in player database."}), 400

    trades.append(trade)

    with open(DATA_FILE, "w") as file:
        json.dump(trades, file, indent=4)

    return jsonify({"message": "Trade successfully submitted!"})
