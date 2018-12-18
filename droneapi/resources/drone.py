from flask_restful import Resource
from flask import jsonify, request

class Drone(Resource):
    DRONES = [
        {
            'name': 'On the Road',
            'model': 'Jack Kerouac',
            'weight': '50',
            'serial_number': '123123-234231-234123',
            'date_acquired': '2018-12-12',
            'new_preowned': 'new',
            'date_registered': '2018-12-12',
        }
    ]

    def get(self):
        response_object = {}
        response_object['drones'] = self.DRONES
        return jsonify(response_object)

    def post(self):
        # response_object = {'status': 'success'}
        post_data = request.get_json()
        self.DRONES.append({
            'name': post_data.get('name'),
            'model': post_data.get('model'),
            'weight': post_data.get('weight'),
            'serial_number': post_data.get('serial_number'),
            'date_acquired': post_data.get('date_acquired'),
            'new_preowned': post_data.get('new_preowned'),
            'date_registered': '2018-12-12',
        })
        response_object = {}
        response_object['message'] = 'Drone added!'
        return jsonify(response_object)


