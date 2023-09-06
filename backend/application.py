
from flask import Flask, jsonify, request
import main

app = Flask(__name__)

# Route to check connection


@app.route("/")
def hello():
    return "Everything looks good"

# Endpoint to get image from client-side


@app.route("/get-image", methods=['POST'])
def getImage():
    if request.method == "POST":
        file = request.files['imageFile']
        imageName = main.compress(file)
        print("in route")

        return jsonify({'prediction': imageName})


if __name__ == "__main__":
    app.run(port=5002)
