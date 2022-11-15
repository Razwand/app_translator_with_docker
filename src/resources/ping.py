from flask_restful import Resource
from flask import jsonify, make_response

class Ping(Resource):
    def get(self):
        response = {"OK": "Servicio ping correcto"}
        return make_response(jsonify(response), 200)
