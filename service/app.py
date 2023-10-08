"""Module to read OS environment variables"""
from os import getenv
from random import randint
import logging
from flask import Flask, jsonify, render_template
from flask.logging import create_logger

app = Flask(__name__)

# Setting app logger from environment variable LOG_LEVEL, if exists. Default is INFO
# Some possible values are: NOTSET, FATAL, CRITICAL, ERROR, INFO, DEBUG
LOG = create_logger(app)
LOG.setLevel(logging.getLevelName(getenv("LOG_LEVEL", logging.getLevelName(logging.INFO))))
LOG.info("Logger configured as %s", logging.getLevelName(LOG.level))

appInfo = {
    "author": "RazorbeakRZ",
    "project": "GotADice",
    "version": "1.0.0",
    "hash": "%HASH%"
}

@app.route("/info")
def app_info():
    """This endpoint return the information of the application"""
    response = appInfo
    return jsonify(response)

@app.route("/")
def frontend_dice_index():
    """ This endpoint returns the generated index.html from the templates folder """
    return render_template('dice-index.html')

@app.route("/roll")
def roll_dice():
    """This endpoint returns a random integer value from 1-6, 
        to simulate the roll of a 6-faces dice"""
    LOG.info("Received request to roll a dice")
    dice_result = randint(1,6)
    LOG.info("Generated value was: %d", dice_result)
    response = { "value": dice_result }
    LOG.debug("Response JSON: %s", response)
    return jsonify(response)

LOG.info("Application started and ready to serve requests")
