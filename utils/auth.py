from functools import wraps

from flask import request, jsonify

from config import conf

def valid_authorization(request):
    authorization_header = request.headers.get('Authorization')
    authorization = conf().get("authorization")
    return authorization_header == authorization


def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not valid_authorization(request):
            return jsonify({"error": "Invalid Authorization header"}), 403
        return f(*args, **kwargs)
    return decorated_function
