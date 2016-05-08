from flask import Flask, render_template, request, redirect, url_for, session

import os

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))



@app.route('/')
def home():
    return render_template('default.html')


@app.route('/showfields/')
def showfields():
    return render_template('showfields.html')


@app.route('/makefield/')
def makefield():
    return render_template('makefield.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
