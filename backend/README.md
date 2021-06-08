# Backend
A simple backend implemented using Flask. This was implemented by modifying the following source: https://cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service 

There are 2 features in this backend. A REST API to infer a text passed to it, and a frontend to interact with it.

## Running the server
To run the server, first install the required dependencies using `pip install -r requirements.txt`. Then run `python main.py` to run the actual server. You can use the virtual environment if you don't want the required files to be installed globally.

## Frontend
You can access the frontend that interacts with the model at the root url `/`.

## API
### Make prediction

Method  : POST
URL: `/infer`
Header: `Content-Type: application/json`
Body: `{"text": "YOUR TEXT HERE"}` 

Response: `{"label1": 0.xxx, ..., "label26": 0.xxx`}
