from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class TextForm(FlaskForm):
    text = StringField('Clippy\'s text', validators=[DataRequired()])
