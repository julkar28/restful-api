from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

app = Flask(__name__)

api = Api(app)

CORS(app)

class Jul(Resource):
    def get(self):
        json_data = request.json
        json = json_data["key"]
        return json
    

api.add_resource(Jul, "/api", methods=["GET"])
if __name__ == "__main__":
    app.run(debug=True,port=5005)
