from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

class FormMessage(FlaskForm):
    firstname = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=100),
        ],
        render_kw={"placeholder": "Firstname"},
    )
    
    lastname = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=100),
        ],
        render_kw={"placeholder": "Lastname"},
    )
    
    email = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=200),
        ],
        render_kw={"placeholder": "Email"},
    )
    
    message = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=500),
        ],
        render_kw={"placeholder": "Message"},
    )

    submit = SubmitField("Register")