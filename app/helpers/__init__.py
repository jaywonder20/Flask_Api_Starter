from flask_restful import reqparse

def send_api_response(response_code, response_message, http_status, response_data={}):
    if http_status not in [200, 201]:
        return {'responseCode': response_code,
                'responseMessage': response_message

                }, int(http_status), \
               {"Access-Control-Allow-Origin": "*"}
    else:
        return {'responseCode': response_code,
                'responseMessage': response_message,
                'data': response_data
                }, int(http_status), \
               {"Access-Control-Allow-Origin": "*"}



parser = reqparse.RequestParser()
parser.add_argument('email_address', help='field cannot be blank.')
