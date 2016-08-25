from flask import Flask, make_response, jsonify

__author__ = "ahmedali"

application = Flask(__name__)


# NOT FOUND Error Handler
@application.errorhandler(404)
def not_found(error):
    return "Page not found! Details: {0}".format(error)


# Bad request
@application.errorhandler(400)
def bad_request():
    return make_response(jsonify(dict(status='error', message='Bad request')), 400)


@application.route('/')
def status():
    return "Hey! It's OK!"


@application.route('/callback')
def callback():
    return "This is a valid callback :)"

