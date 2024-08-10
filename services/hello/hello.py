import logging

from flask import Blueprint

from utils.response import make_success_response
from utils.auth import authorize

hello_serivce = Blueprint("hello", __name__)

@hello_serivce.route("/test", methods=["GET"])
@authorize
def hello_world():
    logging.info("hello world")
    return make_success_response("hello world")
