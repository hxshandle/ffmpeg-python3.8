from flask import Blueprint

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route('/')
def index():
    # return common.say_hello()
    return "hello here is api root 333 "


@bp.route('hello')
def hello():
    return "hello from api"
