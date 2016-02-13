from flask import Flask, render_template, request
from forms import ContactForm
from flask.ext.mail import Message, Mail

app = Flask(__name__)

app.secret_key = 'WebDesign'

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'umsiwebdesign@gmail.com',
    MAIL_PASSWORD = '105sstate',
))

mail = Mail(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/index')   
def home():
    return render_template('index.html', name="index", title="HOME")

@app.route('/q8/<name>')
def q8(name):
  return "<h2>I, %s didn't get any help on this exam</h2>" % name;

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', name="index", title="HOME"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('index.html', name="index", title="HOME"), 500


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
  recipient = [form.email.data]

  if request.method == 'POST':
    msg = Message("Hello", sender="umsiwebdesign@gmail.com", recipients= recipient)
    msg.body = """
    From: %s <%s>
    %s
    """ % (form.name.data, form.email.data, form.message.data)
    mail.send(msg)
    form.name.data = ""
    form.email.data = ""
    form.message.data = ""
    return render_template ('contact.html', form=form, message = "form submitted!")

  elif request.method == 'GET':
    return render_template('contact.html', form=form)

if __name__ == '__main__':
  app.run(debug=True)