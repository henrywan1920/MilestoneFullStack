"""
A predictor to get models and make predictions.
Return marked images and descriptions to the server APIs.
Creating a single function which predicts wether Car is damaged or notCreating a single function which predicts wether Car is damaged or not and localizing the damage, severity of damage for a s and localizing the damage, severity of damage for a single img.
"""
import numpy as np

from keras.utils import load_img, img_to_array
from keras.models import load_model

damaged_or_not_model_path = 'models/densenet_stage1_all-0.917.hdf5'
damage_location_model_path = 'models/densenet_stage2_all-0.667.hdf5'
damage_severity_model_path = 'models/densenet_stage3_all-0.673.hdf5'

Stage_1_model = load_model(damaged_or_not_model_path)
Stage_2_model = load_model(damage_location_model_path)
Stage_3_model = load_model(damage_severity_model_path)


def report(img_path):
    report_pred = []

    img = load_img(img_path, target_size=(256, 256))
    # Converting into array
    img_arr = img_to_array(img)
    img_arr = img_arr.reshape((1,) + img_arr.shape)

    # Checking if Damaged or not
    s1_pred = Stage_1_model.predict(img_arr)
    if s1_pred <= 0.5:
        report_pred.append('Damaged')
    else:
        report_pred.append('Not Damaged')
        return report_pred
    # Checking for Damage Localization
    s2_pred = Stage_2_model.predict(img_arr)
    n = np.argmax(s2_pred)
    if n == 0:
        report_pred.append('Front')
    elif n == 1:
        report_pred.append('Rear')
    else:
        report_pred.append('Side')

    # Checking for Damage Severity
    s3_pred = Stage_3_model.predict(img_arr)
    c = np.argmax(s3_pred)
    if c == 0:
        report_pred.append('Minor')
    elif c == 1:
        report_pred.append('Moderate')
    elif c == 2:
        report_pred.append('Severe')
    return report_pred