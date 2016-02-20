from flask import Flask, render_template, request
from forms import ContactForm

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/client')
def client():
  return render_template('client.html')

@app.route('/student')
def student():
  return render_template('student.html')

# @app.route('/q8/<name>')
# def q8(name):
#   return "<h2>I, %s didn't get any help on this exam</h2>" % name;

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', name="index", title="HOME"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('index.html', name="index", title="HOME"), 500


if __name__ == '__main__':
  app.run(debug=True)