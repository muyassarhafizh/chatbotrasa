# Entity Extraction and Database Query for Chatbot to Help with Food Delivery Status

This project aims to develop a chatbot that can help customers track their food delivery status. The chatbot is capable of extracting relevant information such as the order ID and the customer's location from the user's input using entity extraction techniques. It then queries a database to provide the customer with the latest updates on their food delivery.

## Requirements

The following libraries are required to run the code:

Python 3.6 or above (trained using python 3.10.6)
Flask
spaCy
SQLAlchemy (train using SQLAlchemy 1.4.47)
psycopg2-binary (trained using psycopgr-binary 2.9.6)
rasa (trained using 3.5.4)

To train the chatbot, you can use the following command:

```bash
git clone https://github.com/muyassarhafizh/chatbotrasa.git
pip install -r requirements.txt
rasa train
```

To start the chatbot, run the following command:
```bash
git clone https://github.com/muyassarhafizh/chatbotrasa.git
pip install -r requirements.txt
rasa run actions
```
The last line of code above will run the models action server. To run the model and interact with it  you can run on a separate terminal 
```bash
rasa shell
```

The chatbot supports the following types of queries:

- Track delivery: To track the delivery of an order, the user can enter a message containing their order number.


## Database
 
The data are stored in a PostgreSQL database. The database contains several tables (see Food_Delivery_Database_ERD.png) including orders and deliveries. The orders table stores information about each order, including the order ID, the customer's name, and the order status. The deliveries table stores information about each delivery, including the delivery ID, the order ID, and the delivery status. The chatbot will query the delivery_status column from the delivery tables.

## Future Work
The chatbot can be further improved by adding more features such as:

Natural Language Understanding (NLU): The chatbot can be made more robust by adding more NLU capabilities that enable it to understand the user's intent and generate appropriate responses.
Multi-language support: The chatbot can be made more accessible by adding support for multiple languages.
Integration with delivery service APIs: The chatbot can be made more accurate by integrating with delivery service APIs to obtain real-time information about delivery status.
