import pytest
from app import app
import uuid ,json

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


# User Tests
def test_create_user(client):
    # Dynamically create a unique email
    unique_email = f"user_{uuid.uuid4()}@example.com"  
    
    # Define user data payload
    user_data = {
        'user_name': 'testuser1',
        'email_address': unique_email,
        'user_address': '123 Test St',
        'phone_number': '1234567890'
    }
    
    # Send a POST request to the /users endpoint
    response = client.post('/users', data=json.dumps(user_data), content_type='application/json')
    
    # Validate the response
    assert response.status_code == 201
    assert response.json == {"message": "User created successfully"}



def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_user(client):
    response = client.get('/users/1')  # Assuming there's a user with user_id 1
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test data

def test_update_user(client):
    response = client.put('/users/1', json={
        'user_name': 'updateduser',
        'email_address': 'updated@example.com',
        'user_address': '456 Updated St',
        'phone_number': '0987654321'
    })
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test data

def test_delete_user(client):
    response = client.delete('/users/1')  # Assuming there's a user with user_id 1
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test data




if __name__ == "__main__":
    pytest.main()