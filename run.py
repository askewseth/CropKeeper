from flask import Flask, render_template, request, redirect, url_for, session

import os
from scripts import *

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))



@app.route('/')
def home():
    print APP_ROOT
    return render_template('default.html')


@app.route('/showfields/')
def showfields():
    feilds = getfields()
    # fields = ['test'] * 4
    # fields = [fields]
    return render_template('showfields.html', fields=fields)

@app.route('/template/')
def template():
    return render_template('template.html')


@app.route('/makefield/', methods=['GET', 'POST'])
def makefield():
    if request.method == 'POST':
        loc_ = request.form.get("location", None)
        name_ = request.form.get("feildname", None)

        loc = "-".join(loc_.split())
        name = "-".join(name_.split())

        os.chdir(APP_ROOT + '/static/feilds/')
        os.mkdir(loc + "_" + name)

    return render_template('makefield.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
