from flask import Flask, request, jsonify, g
import mysql.connector
from config import Config  # Import configuration from config.py
from datetime import datetime, timedelta, date  # Import datetime for fine calculation

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



if __name__ == '__main__':
    app.run(debug=True)
