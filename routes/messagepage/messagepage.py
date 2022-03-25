from flask import Blueprint, render_template
from models.contactus import messages

messagepage = Blueprint("messagepage", __name__)


@messagepage.route("/messages", methods=["GET", "POST"])
def mensaje():
    listamensaje = messages.query.all()
    return render_template("messages.html", listamensaje=listamensaje)





