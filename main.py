from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired,Optional,Length,URL
import util
from util import DetailsForm

app=Flask(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = '<ke>'
Bootstrap5(app)


@app.route('/',methods=['GET','POST'])
def estimate_price():
    form=DetailsForm()
    if form.validate_on_submit():
        total_sqft=float(form.area.data)
        location=form.location.data #request.form['location']
        bhk=int(form.bhk.data)#int(request.form['bhk'])
        bath=int(form.bath.data)#int(request.form['bath'])
        response=util.model_estimate_price(location,total_sqft,bhk,bath)
        return render_template('index.html',form=form,response=response,is_=False)
    return render_template('index.html',form=form,is_=True,response='')



if __name__=='__main__':
    app.run(debug=True)
