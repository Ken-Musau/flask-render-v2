# app.py

import os

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Bird

myApp = Flask(__name__)
myApp.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
myApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
myApp.json.compact = False

migrate = Migrate(myApp, db)
db.init_myApp(myApp)

api = Api(myApp)


class Birds(Resource):

    def get(self):
        birds = [bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds), 200)


api.add_resource(Birds, '/birds')
