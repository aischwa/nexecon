from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField

class ContactForm(Form):
	name = TextField("Name", default="")
	email = EmailField("Email", default="")
	message = TextAreaField("Message", default="")
	submit = SubmitField("Send", default="")
