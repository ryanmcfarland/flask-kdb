import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from flask_kdb import FlaskKDB

# Based heavily on - https://github.com/jidn/flask-obscure/blob/master/tests/test_init.py

defaults = {
    "host":"localhost",
    "port":5000 
    }


def make_app(host=None, port=None):
    app = Flask(__name__)

    if host and port:
        app.config["KDB_HOST"] = host
        app.config["KDB_PORT"] = port
    return app

def test_kdb_from_config():
    app = make_app(host=defaults['host'], port=defaults['port'])
    kdb = FlaskKDB(app)

    assert kdb.sendSync("5+5") == 10

def test_kdb_initapp():
    app = make_app(host=defaults['host'], port=defaults['port'])
    kdb = FlaskKDB()
    kdb.init_app(app)

    assert kdb.sendSync("4+4") == 8

# Below test uses the same kdb socket when sending queries
# test.q output:
#"23:14:52.788 | Opening | 5"
#"23:14:52.791 | sync | 5 | 3+2"
#"23:14:52.793 | sync | 5 | 3+3"
#"23:14:52.794 | Closing | 5"
def test_multi_apps():
    app1 = make_app(host=defaults['host'], port=defaults['port'])
    app2 = make_app(host=defaults['host'], port=defaults['port'])

    kdb = FlaskKDB()
    kdb.init_app(app1)
    kdb.init_app(app2)

    @app1.route("/<qry>")
    def index1(qry):
        return str(kdb.sendSync(qry))

    @app2.route("/<qry>")
    def index2(qry):
        return str(kdb.sendSync(qry))
    
    with app1.test_client() as go:
        rv = go.get("/3+2")
        assert 200 == rv.status_code
        assert 5 == int(rv.data)
    
    with app2.test_client() as go:
        rv = go.get("/3+3")
        assert 200 == rv.status_code
        assert 6 == int(rv.data)