from flask import Blueprint, render_template

messagepage = Blueprint("messagepage", __name__)


@messagepage.route("/messages")
def messages():
    return render_template("messages.html")