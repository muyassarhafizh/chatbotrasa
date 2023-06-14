import requests
import os
import logging
import time
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('/app/logAPI/app.log'),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)

class HitRasa(Resource):
    def post(self):
        start_time = time.time()
        json_data = request.get_json()
        message = json_data.get('message')
        sender = json_data.get('sender')
        response = requests.post('http://rasa-app:5005/webhooks/rest/webhook', json={"message":message, "sender":sender})
        response_final =response.json()[0]['text']

        end_time = time.time()
        response_time = end_time - start_time
        logging.info('Hafizh testing : the message took {} seconds to pass'.format(response_time))
        return {"bot": response_final}


api.add_resource(HitRasa, "/hitrasa")
    
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8069')
    app.run(debug=True,port=server_port, host='0.0.0.0')
