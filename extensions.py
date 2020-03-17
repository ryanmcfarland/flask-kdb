from kdb import Kdb_db

## https://stackoverflow.com/questions/55523299/best-practices-for-persistent-database-connections-in-python-when-using-flask

kdb = Kdb_db()
kdb.init_app("test",5001)