from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, DateField,
                    RadioField, SelectField, StringField, TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)


app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

    breed = StringField("What breed are you?", validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():

    form = InfoForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You just clicked the submit button. The breed is {session['breed']}.")
        

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)