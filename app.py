from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

app = Flask(__name__)

api = Api(app)

CORS(app)

class Jul(Resource):
    def get(self):
        token = ""
        api_url = "https://api.telegram.org/bot"+token
        update = request.json
        chatid = update["message"]["chat"]["id"]
        msg = update["message"]["text"]
        if msg == "/start":
            requests.get(api_url+"/sendmessage?chat_id="+str(chatid)+"&text=Haloo, test webhooks dicoffeean.com.&parse_mode=HTML")
        
    

api.add_resource(Jul, "/api", methods=["GET"])
if __name__ == "__main__":
    app.run(debug=True,port=5005)
