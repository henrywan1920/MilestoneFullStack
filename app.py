"""
REST APIs to access the server.
"""
import json
import os
import io
import glob
import subprocess
import logging

from flask import Flask, render_template, request
from PIL import Image
from base64 import encodebytes

from config import BACKEND_URL, LOGGING_LEVEL
from prediction import report


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


def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    return encoded_img


@app.route("/")
@app.route("/index")
def home():
    logger.info("Render template: index.html")
    result_image_path = 'static/ready.png'
    damage_description = 'Ready Go'
    return render_template('index.html', result=result_image_path, description=damage_description)


@app.route("/detection", methods=['POST'])
def detect():
    image = request.files['imagefile']
    image_path = './resources/' + image.filename
    image.save(image_path)

    # Find the latest uploaded image
    uploaded_list_with_boxes = glob.glob('resources/*')
    latest_uploaded_image = max(uploaded_list_with_boxes, key=os.path.getctime)
    latest_uploaded_image_name = image.filename
    logger.info("The latest uploaded image is " + latest_uploaded_image)

    # Get damage description
    preds = report(latest_uploaded_image)

    # Prediction
    # subprocess.run(
    #     ["python", "detect.py", "--weights", "models/car_damage_yolov5.pt", "--img", "416", "--conf", "0.2", "--source",
    #      latest_uploaded_image])
    os.system("python detect.py --weights models/car_damage_yolov5.pt --img 416 --conf 0.2 --source " + latest_uploaded_image)

    # Get the name of the latest output image
    output_list_with_boxes = glob.glob('runs/detect/exp*/' + latest_uploaded_image_name)
    latest_output_image = max(output_list_with_boxes, key=os.path.getctime)
    logger.info("The latest marked image is " + latest_output_image)

    # Generate a brief description to the damage
    if preds[0] == 'Damaged':
        encoded_image = get_response_image(latest_output_image)
        json_object = {"msg": "The vehicle is suffering " + preds[2] + " damages. Below is the type of damage detected.",
                      "encodedImg": '<img src="data:image/png;base64, ' + encoded_image + ' alt="Red dot" style="width:400px;height:400px;" />'}
        logger.info(json.dumps(json_object))
    else:
        json_object = {"msg": "Are you sure the vehicle is damaged?. Please check once."}
        logger.info(json.dumps(json_object))
    damage_description = json_object['msg']

    # Convert the latest output marked image to png and replace static/result.png
    result = Image.open(latest_output_image)
    result.save('static/result.png')
    logger.info('Saved result.png to static')

    # Show the marked image
    result_image_path = 'static/result.png'
    return render_template('index.html', result=result_image_path, description=damage_description)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to
    # AWS EKS, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to docker-compose.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
