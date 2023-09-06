
from flask import Flask, jsonify, request
from flask_cors import CORS

import main

app = Flask(__name__)
CORS(app)


# Route to check connection


@app.route("/")
def hello():
    return "Everything looks good"

# Endpoint to get image from client-side


@app.route("/get-image", methods=['POST'])
def getImage():
    if request.method == "POST":
        file = request.files['imageFile']
        print(file, "file")
        imageName = main.compress(file)
        print("in route")

        return jsonify({'prediction': imageName})


if __name__ == "__main__":
    app.run(port=5002)
