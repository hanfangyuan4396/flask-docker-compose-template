from flask import jsonify

def make_success_response(data) -> dict:
    return jsonify({
        "code": 200,
        "msg": "success",
        "data": data,
        "success": True
    })

def make_error_response(message: str) -> dict:
    return jsonify({
        "code": 500,
        "msg": message,
        "data": None,
        "success": False
    })
