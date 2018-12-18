from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS
from resources.drone import Drone

# Configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
api = Api(app)
app.config.from_object(__name__)

# enable flask_cors
CORS(app)

api.add_resource(Drone, '/drones')
# Health check route


if __name__ == '__main__':
    print("INFO: Starting the app")
    app.run(host='0.0.0.0',port=8090)
