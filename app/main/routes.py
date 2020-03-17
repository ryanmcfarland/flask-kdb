from datetime import datetime
from flask import render_template, flash, redirect, url_for, current_app
from app.main import bp
from extensions import kdb

@bp.route('/', methods=['GET','POST'])
@bp.route('/index',  methods=['GET','POST'])
def index():
    user = {'username': 'Ryan'}
    return render_template('home.html', title="hello", user=user)

# https://stackoverflow.com/questions/43634409/switch-chart-js-data-with-button-click

@bp.route("/chart_flask", methods=['GET','POST'])
def chart_flask():
    conn = kdb.get_db()
    conn.send("hello Ryan")
    var=conn.recv()
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]

    return render_template('chart_flask.html', values=values, labels=labels, legend=legend, var = var)

@bp.route("/chart_kdb", methods=['GET','POST'])
def chart_kdb():
    conn= {"host": "localhost", "port":"5001"}
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart_kdb.html', conn=conn, values=values, labels=labels, legend=legend)