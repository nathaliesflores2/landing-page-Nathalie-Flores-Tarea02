from flask import Blueprint, render_template
from models.contactus import messages
from forms.messageform import FormMessage
from utils.db import db


site = Blueprint("site", __name__)


@site.route("/", methods=["GET", "POST"])
def new_message():
    form = FormMessage()
    if form.validate_on_submit():
            firstname = form.firstname.data
            lastname = form.lastname.data
            email = form.email.data
            message = form.message.data
            nuevo_mensaje = messages(firstname, lastname, email, message)
            db.session.add(nuevo_mensaje)
            db.session.commit()
    return render_template("home.html", form=form)

