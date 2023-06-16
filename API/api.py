import requests
import os
import logging
import time
import uuid
import csv
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
        unique_id = uuid.uuid4()
        start_time = time.time()
        json_data = request.get_json()
        message = json_data.get('message')
        sender = json_data.get('sender')
        response = requests.post('http://rasa-app:5005/webhooks/rest/webhook', json={"message":message, "sender":sender})
        response_final =response.json()[0]['text']
        #TEST
        response2 = requests.post('http://rasa-app:5005/model/parse', json={"text":message}).json()
        intent = response2.get('intent').get('name')
        confidence = response2.get('intent').get('confidence')
        is_fallback = 1 if intent=='nlu_fallback' else 0
        ##END OF TEST
        end_time = time.time()
        response_time = end_time - start_time
        logging.info('Hafizh testing : the message took {} seconds to pass'.format(response_time))
        logging.info('The intent detected  is : {} with confidence of {}'.format(intent, confidence))

        #WRITE TO CSV
        sv = {"id":unique_id, "phone_number":sender, "cust_message":message, "ai_response":response_final, "is_fallback":is_fallback, "intent":intent,"confidence":confidence, "current_threshold":0.98}
        
        with open('/app/data/output.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=sv.keys())
            if csvfile.tell() == 0:  # Check if the file is empty
                writer.writeheader()
            writer.writerow(sv)
        logging.info('Test for csv purposes : {}'.format(sv))
        return {"bot": response_final}


api.add_resource(HitRasa, "/hitrasa")
    
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8069')
    app.run(debug=True,port=server_port, host='0.0.0.0')
