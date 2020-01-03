
import logging
import os
from flask import Flask, escape, request, jsonify
from db import create_connection, db_init, get_state, save_state, remove_state
from utils import titlecase

from werkzeug.utils import import_string


cfg = import_string('config.{env}Config'.format(env=titlecase(os.getenv('FLASK_ENV'))))()
app.config.from_object(cfg)


app = Flask(__name__)
app.logger.setLevel(logging.INFO)
db_init()

@app.route('/vm', methods=['GET', 'POST', 'DELETE'])
def vm():
    if request.method == "GET":
        state = get_state()
        app.logger.info("Getting state {}".format(state))
        return state, 200
    elif request.method == "POST":
        state = request.json
        app.logger.info("Saving state {}".format(state))
        save_state(state)
        return state, 200
    elif request.method == "DELETE":
        app.logger.info("Removing state")
        remove_state()
        return state, 200


@app.route('/vm/lock', methods=['LOCK'])
def lock():
    payload = request.json
    app.logger.info("LOCK reques {}".format(payload))
    return {}, 200


@app.route('/vm/unlock', methods=['UNLOCK'])
def unlock():
    payload = request.json
    app.logger.info("UNLOCK request {}".format(payload))
    return {}, 200

# if __name__ == '__main__':
#     app.run(debug=True)