from flask import Flask
from routes.main.site import site
from routes.messagepage.messagepage import messagepage

app= Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(messagepage)





