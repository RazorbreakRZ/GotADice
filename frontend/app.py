"""Module to read OS environment variables"""
from os import getenv
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
    "project": "GotADice Frontend",
    "version": "1.0.0",
    "hash": "%HASH%"
}

appConfig = {
    "backendUrl": getenv("BACKEND_URL", "http://localhost:5001")
}
LOG.info("Backend url configure as: [%s]", appConfig.get("backendUrl"))

@app.route("/info")
def frontend_info_app():
    """ This endpoint returns a JSON with useful information about the release of the project """
    response = appInfo
    return jsonify(response)

@app.route("/")
def frontend_dice_index():
    """ This endpoint returns the generated index.html from the templates folder """
    return render_template('dice-index.html')

@app.route("/dice-configuration.js")
def frontend_dice_configuration_js():
    """ This endpoint returns the generated configuration JS from the templates folder """
    return render_template('dice-configuration.js',backendUrl=appConfig.get("backendUrl"))

LOG.info("Application started and ready to serve requests")
