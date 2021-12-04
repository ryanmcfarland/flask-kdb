"""

"""
from qpython.qconnection import QConnection

__version__ = "1.0.0"

# https://stackoverflow.com/questions/55523299/best-practices-for-persistent-database-connections-in-python-when-using-flask

class FlaskKDB:
    def __init__(self, app=None, host=None, port=None):
        self.app=app
        self.host=host
        self.port=port
        if app is not None:
            self.init_app(app, self.host, self.port)
        elif host and port:
            self.connect()

    def init_app(self, app, host=None, port=None):
        self.host = host or self.host or app.config["KDB_HOST"]
        self.port = port or self.port or int(app.config["KDB_PORT"])
        self.connect()

    def get_db(self):
        if not self.conn:
            self.connect()
        return self

    def close_db(self):
        if self.conn:
            self.conn.close()

    def connect(self):
        self.conn =  QConnection(host=self.host, port=self.port)
        self.conn.open()

    def sendSync(self, qry):
        if not self.conn:
            self.connect()
        return self.conn.sendSync(qry)