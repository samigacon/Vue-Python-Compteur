from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

compteur = 0

@app.route('/increment', methods=['POST'])
def increment_counter():
    global compteur
    data = request.get_json()
    if data and 'compteur' in data:
        compteur = int(data['compteur'])
        compteur += 1
        response = {
            "compteur": compteur,
            "echo": ["Le compteur a été incrémenté avec succès en Python"]
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "Le contenu de la requête n'est pas au format JSON valide."}), 400

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
