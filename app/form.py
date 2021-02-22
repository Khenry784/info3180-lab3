from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField , TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired

class ContactForm(FlaskForm):
    Name = StringField('Name', validators=[DataRequired("Enter your full name")])
    Subject = StringField('Subject', validators=[DataRequired()])
    Email = EmailField('Email', validators=[DataRequired()])
    Message= TextAreaField('Message',validators=[DataRequired()])