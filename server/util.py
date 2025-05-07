import json
import pickle
# import sklearn
from sklearn.linear_model import LinearRegression
import numpy as np
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Optional,Length,URL
from wtforms import StringField, SubmitField,SelectField,IntegerField

locations=None
model=None
data_columns=None

def model_estimate_price(location,sqft,bhk,bath):
    load_saved_columns()
    load_model()
    try:
        loc_index=data_columns.index(loc_index.lower())
    except:
        loc_index=-1

    x=np.zeros(len(data_columns))
    
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
    return round(model.predict([x])[0],2)


def get_location_names():
    load_saved_columns()
    return locations


def load_saved_columns():
    global locations
    global data_columns
    
    with open(r'C:\Users\linge\Desktop\python 100 days\Machine Learning\reasl Estate\model\columns.json','r') as f:
        data_columns=json.load(f)['data_columns']
        locations=data_columns[3:]
def load_model():
    global model
    with open(r'C:\Users\linge\Desktop\python 100 days\Machine Learning\reasl Estate\model\real_estate_price_prediction_model.pickle','rb') as f:
        model=pickle.load(f)


class DetailsForm(FlaskForm):
    load_saved_columns()
    area = StringField('Area(Square Feet)', validators=[DataRequired()])

    bhk=SelectField(label='BHK',validators=[DataRequired()],choices=["1","2","3","4","5"])
    bath=SelectField(label='BATH',validators=[DataRequired()],choices=["1","2","3","4","5"])
    location=SelectField(label='LOCATIONS',validators=[DataRequired()],choices=[i for i in locations])
    submit = SubmitField('Submit')

# if __name__=='__main__':
#     load_saved_columns()
#     print(get_location_names())
#     print(model_estimate_price('1st phase jp nagar',1000,3,3))
#     print(model_estimate_price('1st phase jp nagar',1000,2,2))
#     print(model_estimate_price('kalhalli',1000,2,2))