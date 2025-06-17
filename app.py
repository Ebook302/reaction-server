from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # מאפשר גישה מה-HTML שלך

# רשימת שחקנים
players = []

@app.route('/submit', methods=['POST'])
def submit_score():
    data = request.json
    players.append(data)
    return jsonify({"message": "Score saved successfully!"})

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    sorted_players = sorted(players, key=lambda x: (x['score'], -x['avgTime']), reverse=True)
    return jsonify(sorted_players)

if __name__ == '__main__':
    app.run(debug=True)
