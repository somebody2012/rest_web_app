import time
from rest_framework_jwt.utils import jwt_decode_handler

def jwt_payload_handler(user):
    return {
        'roles':','.join(['A','B']),
        'username': user.username,
        'exp': time.time() + 60 * 60 * 1000
    }


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'username': "admin",
        'roles':','.join(['A','B']),
        'token': token
    }

