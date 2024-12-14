import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

# Tests for Flask routes
def test_test_db_connection(client):
    rv = client.get('/')
    assert b'Connected to the librarysystem database!' in rv.data or b'Failed to connect' in rv.data







if __name__ == "__main__":
    pytest.main()