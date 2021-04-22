from flask import Flask
from flask_mail import Mail, Message
from src import app
import os

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'maicoljosa920@gmail.com',
    "MAIL_PASSWORD": 'mai21col20'
}

app.config.update(mail_settings)
mail = Mail(app)
