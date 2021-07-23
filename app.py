from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import requests, time

app = Flask(__name__)

api = Api(app)

CORS(app)
r = requests.Session()

class Jul(Resource):
    def get(self):
        #ts = time.time()
        token = "1789568173:AAHN3zAbvbVJmDeAPeHQSOlhynsKAfViVu4"
        api_url = "https://api.telegram.org/bot"+token
        chatid = 836261416
        ers = requests.get(api_url+"/sendmessage?chat_id="+str(chatid)+"&text=Haloo, test webhooks dicoffeean.com.&parse_mode=HTML").text
        #for i in range(20):
        #    r.get("https://shopee.co.id")
        #r.get("https://rest-api-jul.herokuapp.com/api")
        #ts = time.time() - ts
        return ers

    def post(self):
        token = "1789568173:AAHN3zAbvbVJmDeAPeHQSOlhynsKAfViVu4"
        api_url = "https://api.telegram.org/bot"+token
        update = request.json
        chatid = update["message"]["chat"]["id"]
        msg = update["message"]["text"]
        if msg == "/start":
            while True:
                return 0
                #requests.get(api_url+"/sendmessage?chat_id="+str(chatid)+"&text=Haloo, test webhooks dicoffeean.com.&parse_mode=HTML")
        
    

api.add_resource(Jul, "/api", methods=["GET","POST"])
if __name__ == "__main__":
    app.run(debug=True,port=5005)
