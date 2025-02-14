from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore


from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask server is running!"  # Ensure this message is correct

if __name__ == "__main__":
    app.run(debug=True)



app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate("firebase_config.json")  # Path to your key file
firebase_admin.initialize_app(cred)
db = firestore.client()  # Firestore database instance

@app.route("/")
def home():
    return jsonify({"message": "Firebase connected!"})

@app.route("/add", methods=["POST"])
def add_data():
    data = request.json  # Example: {"name": "John", "age": 25}
    doc_ref = db.collection("users").add(data)
    return jsonify({"message": "Data added!", "id": doc_ref[1].id})

@app.route("/get", methods=["GET"])
def get_data():
    users = db.collection("users").stream()
    user_list = [{doc.id: doc.to_dict()} for doc in users]
    return jsonify(user_list)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
