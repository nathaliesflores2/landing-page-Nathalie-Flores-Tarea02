from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from routes.main.site import site
from routes.messagepage.messagepage import messagepage

app= Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

app.register_blueprint(site)
app.register_blueprint(messagepage)





