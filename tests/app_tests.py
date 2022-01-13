from nose.tools import *
from app import app
from sqlalchemy import create_engine, text
import code

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)

def test_missing_pages():
    rv = web.get('/contact', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rv = web.get('/login', follow_redirects=True)
    assert_equal(rv.status_code, 404)


class localdb():
    def __init__(self):
        self.engine = None
        try:
            self.engine = create_engine('mysql+pymysql://root:root@localhost:3307/flaskballetcasting')
        except Exception as e: 
            self.engine = create_engine('mysql+pymysql://root:root@localhost:3306/flaskballetcasting')
            print('could not connect to localhost database because bad port' + str(e))

    def get_locations(self) -> tuple:
        """
        Get data from the locations table, the column names and the rows in a tuple of 2 lists
        """
        with self.engine.connect() as conn:
            rows = conn.execute(text("select * from locations;")) 
            column_table = conn.execute(text("show columns in locations;")) 
            columns = [i[0] for i in column_table] 
        return columns, rows


code.interact(local=locals)