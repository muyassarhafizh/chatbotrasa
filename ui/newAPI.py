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

# @app.route('/new-api', methods=['POST'])
# def hit_external_api():
#     input_data = requests.json
#     # send data to external API
#     response = requests.post('https://acda-103-125-37-137.ngrok-free.app/webhooks/rest/webhook', data=input_data)

#     # parse response
#     response_final =response.json()[0]['text']

#     # # extract JSON objects from array
#     # json_list = []
#     # for item in response_dict['items']:
#     #     json_list.append(item['json_data'])

#     # return JSON response
#     return jsonify(response)
    
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8069')
    app.run(debug=True,port=server_port)