import json
import os

from flask import Flask, render_template

from config import BACKEND_URL, LOGGING_LEVEL

import logging
logger = logging.getLogger()
if LOGGING_LEVEL == 'INFO':
    logger.setLevel(logging.INFO)
elif LOGGING_LEVEL == 'ERROR':
    logger.setLevel(logging.ERROR)
elif LOGGING_LEVEL == 'DEBUG':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.WARNING)

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def home():
    default_image_path = os.path.join('static', 'result.png')
    logger.info("Render template: index.html")
    return render_template('index.html', image0=default_image_path)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to
    # AWS EKS, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to docker-compose.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)