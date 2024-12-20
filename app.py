from flask import Flask, request, jsonify, g
import mysql.connector
from config import Config  # Import configuration from config.py
from datetime import datetime, timedelta, date  # Import datetime for fine calculation
from flask_jwt_extended import JWTManager, create_access_token, jwt_required  # Import JWT related functions

app = Flask(__name__)

# Database connection function using the configuration from config.py
def get_db_connection():
    if 'db' not in g:
        try:
            g.db = mysql.connector.connect(
                host=Config.MYSQL_HOST,
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD,
                database=Config.MYSQL_DB
            )
        except mysql.connector.Error as err:
            return None
    return g.db

jwt = JWTManager(app)  # Initialize JWTManager with the app

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == 'laquiorez' and data['password'] == '286unseen':
        access_token = create_access_token(identity='admin')
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.teardown_appcontext
def close_db_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Sample route to test the database connection
@app.route('/')
def test_db_connection():
    connection = get_db_connection()
    if connection.is_connected():
        return "Connected to the librarysystem database!"
    return "Failed to connect"

# CREATE: Add a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    # Input validation
    if not data or not data.get('user_name') or not data.get('email_address'):
        return jsonify({"error": "Bad Request: Missing required fields"}), 400

    user_name = data['user_name']
    email_address = data['email_address']

    connection = get_db_connection()
    cursor = connection.cursor()

    # Insert the user into the database
    cursor.execute('INSERT INTO users (user_id, user_name, user_address, email_address, phone_number) VALUES (NULL, %s, %s, %s, %s)', 
                   (user_name, data.get('user_address'), email_address, data.get('phone_number')))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "User created successfully"}), 201

# READ: Get all users
@app.route('/users', methods=['GET'])
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor()
 
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    cursor.close()
    connection.close()

    # If no users exist
    if not users:
        return jsonify({"message": "No users found"}), 404

    return jsonify(users), 200

# READ: Get a specific user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE user_id = %s', (id,))
    user = cursor.fetchone()

    cursor.close()
    connection.close()

    # If the user is not found
    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user), 200

# UPDATE: Modify a user's information by ID
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()

    if not data or not data.get('user_name') or not data.get('email_address'):
        return jsonify({"error": "Bad Request: Missing required fields"}), 400

    user_name = data['user_name']
    email_address = data['email_address']

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('UPDATE users SET user_name = %s, email_address = %s, user_address = %s, phone_number = %s WHERE user_id = %s', 
                   (user_name, email_address, data.get('user_address'), data.get('phone_number'), id))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "User updated successfully"}), 200

# DELETE: Delete a user by ID
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM users WHERE user_id = %s', (id,))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "User deleted successfully"}), 200

# CREATE: Add a new loan
@app.route('/loans', methods=['POST'])
def create_loan():
    data = request.get_json()

    # Input validation
    if not data or not data.get('user_id') or not data.get('isbn') or not data.get('date_issued') or not data.get('date_due_for_return'):
        return jsonify({"error": "Bad Request: Missing required fields"}), 400

    user_id = data['user_id']
    isbn = data['isbn']
    date_issued = data['date_issued']
    date_due_for_return = data['date_due_for_return']
    date_returned = data.get('date_returned')  # Optional field

    connection = get_db_connection()
    cursor = connection.cursor()

    # Insert the loan into the database
    cursor.execute('INSERT INTO loans (user_id, isbn, date_issued, date_due_for_return, date_returned) VALUES (%s, %s, %s, %s, %s)', 
                   (user_id, isbn, date_issued, date_due_for_return, date_returned))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Loan created successfully"}), 201

# READ: Get all loans
@app.route('/loans', methods=['GET'])
def get_loans():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM loans')
    loans = cursor.fetchall()

    cursor.close()
    connection.close()

    # Calculate fines for each loan
    loans_with_fines = []
    total_fine = 0  # Initialize total fine
    for loan in loans:
        due_date = loan[4]  # Assuming the due date is in the 5th column
        fine = calculate_overdue_fines(due_date)
        loans_with_fines.append({
            "loan": loan,
            "fine": fine
        })
        total_fine += fine  # Accumulate total fine

    # If no loans exist
    if not loans:
        return jsonify({"message": "No loans found"}), 404

    return jsonify({"loans": loans_with_fines, "total_fine": total_fine}), 200  # Include total fine in response

# READ: Get a specific loan by ID
@app.route('/loans/<int:id>', methods=['GET'])
def get_loan(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM loans WHERE book_borrowing_id = %s', (id,))
    loan = cursor.fetchone()

    cursor.close()
    connection.close()

    # If the loan is not found
    if loan is None:
        return jsonify({"error": "Loan not found"}), 404

    return jsonify(loan), 200

# UPDATE: Modify a loan's information by ID
@app.route('/loans/<int:id>', methods=['PUT'])
def update_loan(id):
    data = request.get_json()

    if not data or not data.get('user_id') or not data.get('isbn'):
        return jsonify({"error": "Bad Request: Missing required fields"}), 400

    user_id = data['user_id']
    isbn = data['isbn']
    date_returned = data.get('date_returned')  # Optional field

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('UPDATE loans SET user_id = %s, isbn = %s, date_returned = %s WHERE book_borrowing_id = %s', 
                   (user_id, isbn, date_returned, id))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Loan updated successfully"}), 200

# DELETE: Delete a loan by ID
@app.route('/loans/<int:id>', methods=['DELETE'])
def delete_loan(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM loans WHERE book_borrowing_id = %s', (id,))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Loan deleted successfully"}), 200

# Function to calculate overdue fines
def calculate_overdue_fines(due_date):
    # Convert due_date to datetime if it's a date
    if isinstance(due_date, date) and not isinstance(due_date, datetime):
        due_date = datetime.combine(due_date, datetime.min.time())
        
    if due_date < datetime.now():
        overdue_days = (datetime.now() - due_date).days
        fine_per_day = 1  # Example fine amount
        return overdue_days * fine_per_day
    return 0

# CREATE: Add a new library rule
@app.route('/rules', methods=['POST'])
def create_rule():
    data = request.get_json()

    # Input validation
    if not data or not data.get('rule_id') or not data.get('rule_description') or not data.get('rule_value'):
        return jsonify({"error": "Bad Request: Missing required fields"}), 400

    rule_id = data['rule_id']
    rule_description = data['rule_description']
    rule_value = data['rule_value']

    connection = get_db_connection()
    cursor = connection.cursor()

    # Insert the rule into the database
    cursor.execute('INSERT INTO library_rules (rule_id, rule_description, rule_value) VALUES (%s, %s, %s)', 
                   (rule_id, rule_description, rule_value))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Rule created successfully"}), 201

# READ: Get all library rules
@app.route('/rules', methods=['GET'])
def get_rules():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM library_rules')
    rules = cursor.fetchall()

    cursor.close()
    connection.close()

    # If no rules exist
    if not rules:
        return jsonify({"message": "No rules found"}), 404

    return jsonify(rules), 200

# READ: Get a specific library rule by ID
@app.route('/rules/<int:rule_id>', methods=['GET'])
def get_rule(rule_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM library_rules WHERE rule_id = %s', (rule_id,))
    rule = cursor.fetchone()

    cursor.close()
    connection.close()

    # If the rule is not found
    if rule is None:
        return jsonify({"error": "Rule not found"}), 404

    return jsonify(rule), 200

# UPDATE: Modify a library rule's information by ID
@app.route('/rules/<int:rule_id>', methods=['PUT'])
def update_rule(rule_id):
    data = request.get_json()

    if not data or not data.get('rule_description') or not data.get('rule_value'):
        return jsonify({"error": "Bad Request: Missing required fields"}), 400

    rule_description = data['rule_description']
    rule_value = data['rule_value']

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('UPDATE library_rules SET rule_description = %s, rule_value = %s WHERE rule_id = %s', 
                   (rule_description, rule_value, rule_id))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Rule updated successfully"}), 200

# DELETE: Delete a library rule by ID
@app.route('/rules/<int:rule_id>', methods=['DELETE'])
def delete_rule(rule_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM library_rules WHERE rule_id = %s', (rule_id,))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Rule deleted successfully"}), 200


# CREATE: Add a new category
@app.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    category_name = data.get('category_name')

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO categories (category_name) VALUES (%s)', (category_name,))
    connection.commit()

    category_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({"message": "Category created successfully", "category_id": category_id}), 201


# READ: Get all categories
@app.route('/categories', methods=['GET'])
def get_categories():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()

    cursor.close()
    connection.close()

    # If no categories exist
    if not categories:
        return jsonify({"message": "No categories found"}), 404

    return jsonify(categories), 200

# READ: Get a specific category by ID
@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM categories WHERE category_id = %s', (category_id,))
    category = cursor.fetchone()

    cursor.close()
    connection.close()

    # If the category is not found
    if category is None:
        return jsonify({"error": "Category not found"}), 404

    return jsonify(category), 200

# UPDATE: Modify a category's information by ID
@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.get_json()

    if not data or not data.get('category_name'):
        return jsonify({"error": "Bad Request: Missing required fields"}), 400

    category_name = data['category_name']

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('UPDATE categories SET category_name = %s WHERE category_id = %s', 
                   (category_name, category_id))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Category updated successfully"}), 200

# DELETE: Delete a category by ID
@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM categories WHERE category_id = %s', (category_id,))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Category deleted successfully"}), 200


# CREATE: Add a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()

    # Input validation
    if not data or not data.get('isbn') or not data.get('book_title') or not data.get('date_of_publication') or not data.get('category_id'):
        return jsonify({"error": "Bad Request: Missing required fields"}), 400

    isbn = data['isbn']
    book_title = data['book_title']
    date_of_publication = data['date_of_publication']
    category_id = data['category_id']

    connection = get_db_connection()
    cursor = connection.cursor()

    # Insert the book into the database
    cursor.execute('INSERT INTO books (isbn, book_title, date_of_publication, category_id) VALUES (%s, %s, %s, %s)', 
                   (isbn, book_title, date_of_publication, category_id))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Book created successfully"}), 201

# READ: Get all books
@app.route('/books', methods=['GET'])
def get_books():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()

    cursor.close()
    connection.close()

    # If no books exist
    if not books:
        return jsonify({"message": "No books found"}), 404

    return jsonify(books), 200

# READ: Get a specific book by ISBN
@app.route('/books/<string:isbn>', methods=['GET'])
def get_book(isbn):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books WHERE isbn = %s', (isbn,))
    book = cursor.fetchone()

    cursor.close()
    connection.close()

    # If the book is not found
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    return jsonify(book), 200

# UPDATE: Modify a book's information by ISBN
# UPDATE: Modify a book's information by ISBN
@app.route('/books/<string:isbn>', methods=['PUT'])
def update_book(isbn):
    data = request.get_json()

    # Input validation
    if not data or not data.get('book_title') or not data.get('date_of_publication') or not data.get('category_id'):
        return jsonify({"error": "Bad Request: Missing required fields"}), 400

    book_title = data['book_title']
    date_of_publication = data['date_of_publication']
    category_id = data['category_id']

    # Check if the category exists
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT COUNT(*) FROM categories WHERE category_id = %s', (category_id,))
    category_exists = cursor.fetchone()[0]

    if not category_exists:
        cursor.close()
        connection.close()
        return jsonify({"error": "Bad Request: Category does not exist"}), 400

    # Update the book details in the database
    cursor.execute('UPDATE books SET book_title = %s, date_of_publication = %s, category_id = %s WHERE isbn = %s', 
                   (book_title, date_of_publication, category_id, isbn))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Book updated successfully"}), 200


# DELETE: Delete a book by ISBN
@app.route('/books/<string:isbn>', methods=['DELETE'])
def delete_book(isbn):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE isbn = %s', (isbn,))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Book deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
