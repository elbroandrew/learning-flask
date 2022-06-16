from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddOwnerForm(FlaskForm):
    name = StringField('Name of Owner')
    pup_id = IntegerField('ID of Puppy: ')
    submit = SubmitField("Add Owner")