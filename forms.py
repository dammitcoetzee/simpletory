from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField
from wtforms.validators import DataRequired

class Add_Item(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    image = FileField()