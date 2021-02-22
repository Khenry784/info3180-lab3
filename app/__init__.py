from flask import Flask, url_for
from flask_mail import Mail
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'd9d54d3cf23f20'
app.config['MAIL_PASSWORD'] = '3d289a76546f33'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail= Mail(app)
from app import views