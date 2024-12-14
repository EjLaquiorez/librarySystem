---

# Library Management System API

This is a **Flask-based API** designed to manage a library system. It allows administrators and users to interact with books, loans, users, rules, and categories. The system supports functionalities such as borrowing books, calculating overdue fines, categorizing books, and managing library rules.

## Features

- **User Management**: Add, update, delete, and fetch user information.
- **Book Management**: Manage books, including titles, ISBNs, and publication details.
- **Loan Management**: Create and manage loans, track due dates, and calculate overdue fines.
- **Category Management**: Categorize books by genres or sections.
- **Library Rules**: Define and enforce rules such as overdue fines.
- **Fine Calculation**: Automatically calculate overdue fines based on return dates.

---

## Project Setup

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone <repository-link>
cd library-management-system
```

### 2. Create a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
    ```bash
    .\venv\Scripts\activate
    ```
- **macOS/Linux**:
    ```bash
    source venv/bin/activate
    ```

### 3. Install Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Update the database credentials in a `config.py` file:

```python
class Config:
    MYSQL_HOST = "localhost"
    MYSQL_USER = "your_username"
    MYSQL_PASSWORD = "your_password"
    MYSQL_DB = "librarysystem"
```

Make sure you have a MySQL database named `librarysystem` created.

### 5. Run the Application

Start the Flask development server:

```bash
python app.py
```

The server will start on `http://127.0.0.1:5000`.

---

## API Endpoints

### User Management

- **Create a User**
    - Method: `POST`
    - URL: `/users`
    - Body:
      ```json
      {
        "user_name": "John Doe",
        "user_address": "123 Main St",
        "email_address": "john.doe@example.com",
        "phone_number": "123456789"
      }
      ```
    - Response: `{"message": "User created successfully"}`

- **Get All Users**
    - Method: `GET`
    - URL: `/users`

- **Get User by ID**
    - Method: `GET`
    - URL: `/users/<id>`

- **Update User**
    - Method: `PUT`
    - URL: `/users/<id>`

- **Delete User**
    - Method: `DELETE`
    - URL: `/users/<id>`

---

### Book Management

- **Create a Book**
    - Method: `POST`
    - URL: `/books`
    - Body:
      ```json
      {
        "isbn": "9782345678901",
        "book_title": "Sample Book Title",
        "date_of_publication": "2023-10-01",
        "category_id": 1
      }
      ```

- **Get All Books**
    - Method: `GET`
    - URL: `/books`

- **Get Book by ISBN**
    - Method: `GET`
    - URL: `/books/<isbn>`

- **Update Book**
    - Method: `PUT`
    - URL: `/books/<isbn>`

- **Delete Book**
    - Method: `DELETE`
    - URL: `/books/<isbn>`

---

### Loan Management

- **Create a Loan**
    - Method: `POST`
    - URL: `/loans`
    - Body:
      ```json
      {
        "user_id": 1,
        "isbn": "9782345678901",
        "date_issued": "2023-10-01",
        "date_due_for_return": "2023-10-15"
      }
      ```

- **Get All Loans**
    - Method: `GET`
    - URL: `/loans`

- **Update Loan (Return Book)**
    - Method: `PUT`
    - URL: `/loans/<loan_id>`
    - Body:
      ```json
      {
        "user_id": 1,
        "isbn": "9782345678901",
        "date_returned": "2023-10-20"
      }
      ```

---

### Rule Management

- **Create a Rule**
    - Method: `POST`
    - URL: `/rules`
    - Body:
      ```json
      {
        "rule_id": 1,
        "rule_description": "Overdue fine of $1 per day.",
        "rule_value": 1
      }
      ```

- **Get All Rules**
    - Method: `GET`
    - URL: `/rules`

---

### Category Management

- **Create a Category**
    - Method: `POST`
    - URL: `/categories`
    - Body:
      ```json
      {
        "category_name": "Fiction"
      }
      ```

- **Get All Categories**
    - Method: `GET`
    - URL: `/categories`

---

## Fine Calculation

The system calculates overdue fines automatically when fetching loan data. The fine is calculated as:

```
Fine = (Current Date - Due Date) * $1 per day
```

---

## Project Structure

```bash
library-management-system/
├── app.py                # Main application file
├── config.py             # Configuration file (database credentials)
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## Testing the API

You can use tools like **Postman** or **curl** to interact with the API. Here's an example request for creating a loan:

```bash
curl -X POST http://127.0.0.1:5000/loans -H "Content-Type: application/json" -d '{
  "user_id": 1,
  "isbn": "9782345678901",
  "date_issued": "2023-10-01",
  "date_due_for_return": "2023-10-15"
}'
```

---

## Troubleshooting

1. **Database Connection Issue**:
   - Ensure your MySQL service is running.
   - Verify the credentials in `config.py`.

2. **Missing Dependencies**:
   - Run `pip install -r requirements.txt`.

3. **Port Already in Use**:
   - Stop other processes using port 5000 or run the app on a different port.

---

## License

This project is licensed under the MIT License.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -am "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

--- 

This README provides clear setup instructions, API endpoint details, and helpful troubleshooting tips for anyone working on or using the library system.
