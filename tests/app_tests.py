from nose.tools import *
from app import app

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
