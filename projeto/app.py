import flask
import os
from flask import Flask, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

URL = os.getenv('DB_URL')
USER = os.getenv('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/url')
def url():
    return f"URL: {URL}"
@app.route('/user')
def user():
    return f"USER: {USER}"
@app.route('/password')
def password():
    return f"PASSWORD: {PASSWORD}"

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port="5000")