from wtforms import StringField
from flask.ext.wtf import Form 
from wtforms.validators import DataRequired

class InputForm(Form):
	inputWord = StringField('inputWord',validators=[DataRequired()])