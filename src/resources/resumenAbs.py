from flask import request, jsonify, make_response
from flask_restful import Resource
from tools.translate_my_subs import *   # Cambiar por funciones concretas si es necesario en lugar de todo el namespace

class ResumenAbs(Resource):
    def post(self):
        if "file" in request.files:
            try:
                input_data = request.files["file"].read().decode("latin-1")
            except:
                input_data = None
        else:
            input_data = request.get_json().get("text", "")
        if not input_data:
            return make_response(jsonify(errmsg="input_data is empty or there was an error on file reading"), 417)
        try:
            rdata = main_translator(input_data)  # Devuelve el diccionario "predictions.json"
        except Exception as e:
            return make_response(jsonify(errmsg=str(e)), 500)
        return make_response(jsonify(rdata), 200)