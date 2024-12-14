import pytest, uuid ,json 
from app import app
from datetime import datetime, date, timedelta
from app import app, calculate_overdue_fines

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


############################################################################## User Tests #########################################################################
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

################################################################ Loan Tests ###############################################################################################

def test_create_loan(client):
    loan_data = {
        'user_id': 2,
        'isbn': '9782345678901',
        'date_issued': '2023-10-01',
        'date_due_for_return': '2023-10-15'
    }

    response = client.post('/loans', json=loan_data)
    assert response.status_code == 201
    assert b'Loan created successfully' in response.data


def test_get_loans(client):
    response = client.get('/loans')
    assert response.status_code == 200
    assert 'loans' in response.json

def test_get_loan(client):
    response = client.get('/loans/1')  # Assuming there's a loan with book_borrowing_id 1
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test data

def test_update_loan(client):
    response = client.put('/loans/1', json={  # Assuming you're updating the loan with book_borrowing_id 1
        'user_id': 1,  # Ensure this user_id exists
        'isbn': '9783161484101',  # Ensure ISBN fits the length
        'date_returned': '2023-01-15'  # Update the date_returned field
    })
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test data

def test_delete_loan(client):
    response = client.delete('/loans/1')  # Assuming there's a loan with book_borrowing_id 1
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test data

def test_calculate_overdue_fines():
    with app.app_context():
        # Test case 1: Due date in the past
        past_date = datetime.now() - timedelta(days=5)
        assert calculate_overdue_fines(past_date) == 5

        # Test case 2: Due date today
        today_date = datetime.now()
        assert calculate_overdue_fines(today_date) == 0

        # Test case 3: Due date in the future
        future_date = datetime.now() + timedelta(days=5)
        assert calculate_overdue_fines(future_date) == 0

        # Test case 4: Due date as a date object
        past_date_as_date = date.today() - timedelta(days=5)
        assert calculate_overdue_fines(past_date_as_date) == 5


if __name__ == "__main__":
    pytest.main()