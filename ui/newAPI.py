import requests
import os
from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HitRasa(Resource):
    def post(self,message):
        response = requests.post('https://5a84-103-125-37-137.ngrok-free.app/webhooks/rest/webhook', json={"message":message})
        response_final =response.json()[0]['text']
        return {"bot": response_final}

api.add_resource(HitRasa, "/hitrasa/<string:message>")
    
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8069')
    app.run(debug=True,port=server_port, host='0.0.0.0')