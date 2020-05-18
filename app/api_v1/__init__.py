from flask_restful_swagger_2 import Resource, swagger, Schema
from app.helpers import *
import logging


class UserEmail(Schema):
    type = 'object'
    properties = {
        'email_address': {
            'type': 'string',

        }
    }
    required = ['email_address']


class TestEndpoint(Resource):

    @swagger.doc({
        'tags': ['test'],
        'description': 'Description for test endpoint',
        'parameters': [
            {
                'name': 'request',
                'description': 'Test',
                'in': 'body',
                'schema': UserEmail,

                'type': 'json'
            },

        ],
        'responses': {
            '200': {
                'description': 'User',

                'examples': {
                    'S01': {
                        "responseCode": "S01",
                        "responseMessage": "a dummy response messae",
                        "data": {}
                    }
                }
            },
            '500': {
                'description': 'Server Error',

                'examples': {
                    'S05': {
                        "responseCode": "SO5",
                        "responseMessage": "Something went wrong",
                        "data": {}
                    }
                }
            }
        }
    })
    def post(self):
        try:

            data = parser.parse_args()
            print(data)

            email_address = data["email_address"]

            return send_api_response("S01", "Server Response ", 200, {
                "email_address": email_address

            })

        except:
            logging.error("Fatal error in main loop", exc_info=True)

            return send_api_response("S05", "OOPS something went wrong", 500)
