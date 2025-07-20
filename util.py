import os
import json
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, SelectField

# Globals
locations = None
model = None
data_columns = None

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COLUMNS_PATH = os.path.join(BASE_DIR, 'model', 'columns.json')
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'real_estate_price_prediction_model.pickle')

def model_estimate_price(location, sqft, bhk, bath):
    load_saved_columns()
    load_model()
    try:
        loc_index = data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(model.predict([x])[0], 2)


def get_location_names():
    load_saved_columns()
    return locations


def load_saved_columns():
    global locations, data_columns
    with open(COLUMNS_PATH, 'r') as f:
        data_columns = json.load(f)['data_columns']
        locations = data_columns[3:]


def load_model():
    global model
    if model is None:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)


class DetailsForm(FlaskForm):
    area = StringField('Area (Square Feet)', validators=[DataRequired()])
    bhk = SelectField('BHK', validators=[DataRequired()], choices=[str(i) for i in range(1, 6)])
    bath = SelectField('Bath', validators=[DataRequired()], choices=[str(i) for i in range(1, 6)])
    location = SelectField('Location', validators=[DataRequired()], choices=[])
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(DetailsForm, self).__init__(*args, **kwargs)
        load_saved_columns()
        self.location.choices = [(loc, loc) for loc in locations]
