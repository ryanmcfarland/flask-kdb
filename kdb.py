from websocket import create_connection

class Kdb_db:
    def __init__(self):
        self.app=None
        self.connection=None
        self.port=None

    def init_app(self, app, port):
        self.app = app
        self.port = port
        self.connect()
    
    def connect(self):
        self.connection = create_connection("ws://localhost:"+str(self.port))
        return self.connection
    
    def get_db(self):
        if not self.connection:
            return self.connect()
        return self.connection