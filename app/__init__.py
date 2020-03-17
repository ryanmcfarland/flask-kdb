from flask import Flask, current_app, g
from flask_bootstrap import Bootstrap
from extensions import kdb
import logging

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    #kdb.init_app(app, 5000)
    bootstrap.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app