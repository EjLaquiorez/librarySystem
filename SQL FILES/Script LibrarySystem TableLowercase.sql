-- Create the users table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    user_address VARCHAR(255),
    email_address VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(15)
);

-- Create the books table
CREATE TABLE books (
    isbn VARCHAR(13) PRIMARY KEY,
    book_title VARCHAR(255) NOT NULL,
    date_of_publication DATE
);

-- Create the authors table
CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_firstname VARCHAR(255) NOT NULL,
    author_surname VARCHAR(255) NOT NULL
);

-- Create the books_authors junction table
CREATE TABLE books_authors (
    book_author_id INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13) NOT NULL,
    author_id INT NOT NULL,
    FOREIGN KEY (isbn) REFERENCES books(isbn) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE
);

-- Create the categories table
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL UNIQUE
);

-- Add a foreign key in the books table to reference categories
ALTER TABLE books
ADD category_id INT,
ADD FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE SET NULL;

-- Create the loans table
CREATE TABLE loans (
    book_borrowing_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    isbn VARCHAR(13) NOT NULL,
    date_issued DATE NOT NULL,
    date_due_for_return DATE NOT NULL,
    date_returned DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (isbn) REFERENCES books(isbn) ON DELETE CASCADE
);

-- Create the library_rules table
CREATE TABLE library_rules (
    rule_id INT AUTO_INCREMENT PRIMARY KEY,
    rule_description VARCHAR(255) NOT NULL,
    rule_value DECIMAL(10, 2) NOT NULL
);
