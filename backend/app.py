from flask import Flask, jsonify
from flask.logging import create_logger
from random import randint
import logging
import os

app = Flask(__name__)

# Setting app logger from environment variable LOG_LEVEL, if exists. Default is INFO
# Some possible values are: NOTSET, FATAL, CRITICAL, ERROR, INFO, DEBUG
LOG = create_logger(app)
LOG.setLevel(logging.getLevelName(os.getenv("LOG_LEVEL", logging.INFO)))
LOG.info(f"Logger configured as {logging.getLevelName(LOG.level)}")


@app.route("/info")
def app_info():
    return { 
        "author": "RazorbeakRZ" ,
        "version": "0.0.1"
    }

@app.route("/roll")
def roll_dice():
    LOG.info("Received request to roll a dice")
    dice_result = randint(1,6)
    LOG.info(f"Generated value was: {dice_result}")
    response = { "value": dice_result }
    LOG.debug(f"Response JSON: {response}")
    return jsonify(response)

LOG.info(f"Application started and ready to serve requests")