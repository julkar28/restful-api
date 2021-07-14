from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

app = Flask(__name__)

api = Api(app)

CORS(app)

class Jul(Resource):
    def get(self):
        response = {"msg": requests.get('https://carnine.000webhostapp.com/kontak').json()}
        return response
    

api.add_resource(Jul, "/api", methods=["GET"])
if __name__ == "__main__":
    app.run(debug=True,port=5005)