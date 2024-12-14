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

########################################################### Rule Tests ###################################################################
def test_create_rule(client):
    response = client.post('/rules', json={
        'rule_id': 1,
        'rule_description': 'No loud noises',
        'rule_value': 1  # Assuming rule_value is numeric
    })
    assert response.status_code == 201
    assert b'Rule created successfully' in response.data

def test_get_rules(client):
    response = client.get('/rules')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_rule(client):
    response = client.get('/rules/1')  # Assuming there's a rule with rule_id 1
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test data

def test_update_rule(client):
    response = client.put('/rules/1', json={
        'rule_description': 'No loud noises',
        'rule_value': 2  # Assuming rule_value is numeric
    })
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test data

def test_delete_rule(client):
    response = client.delete('/rules/1')  # Assuming there's a rule with rule_id 1
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test data


################################################################# Category Tests ###########################################################################
def test_create_category(client):
    try:
        unique_category_name = f'Unique Category {uuid.uuid4()}'  # Ensure unique category name
        response = client.post('/categories', json={
            'category_name': unique_category_name
        })
        assert response.status_code == 201
        assert b'Category created successfully' in response.data
    except Exception as e:
        pytest.fail(f"Error creating category: {str(e)}")

def test_get_categories(client):
    response = client.get('/categories')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_category(client):
    response = client.get('/categories/1')  # Assuming there's a category with category_id 1
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test data

def test_update_category(client):
    response = client.put('/categories/1', json={
        'category_name': 'Updated Category'
    })
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test data

def test_delete_category(client):
    response = client.delete('/categories/1')  # Assuming there's a category with category_id 1
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test data


######################################################################### Book Tests #############################################################################
def create_category(client):
    unique_category_name = f'Unique Category {uuid.uuid4()}'  # Ensure unique category name
    response = client.post('/categories', json={
        'category_name': unique_category_name
    })
    assert response.status_code == 201
    assert 'category_id' in response.json, "Response does not include 'category_id'"  # Ensure category_id is present
    return response.json.get('category_id')  # Retrieve category_id


def test_get_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_book(client):
    response = client.get('/books/9780001122334')  # Assuming there's a book with this ISBN
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test data

def test_update_book(client):
    try:
        unique_category_name = f'Unique Updated Books Category {uuid.uuid4()}'  # Ensure unique category name
        response = client.put('/books/9783161484101', json={
            'isbn': '9783161484101',  # Ensure ISBN fits the length
            'book_title': 'Updated Book',
            'date_of_publication': '2022-01-02',
            'category_id': 2  # Ensure the category_id exists
        })
        assert response.status_code == 200 or response.status_code == 404
    except Exception as e:
        pytest.fail(f"Error updating book: {str(e)}")

def test_delete_book(client):
    response = client.delete('/books/9780001122334')  # Assuming there's a book with this ISBN
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test data

if __name__ == "__main__":
    pytest.main()