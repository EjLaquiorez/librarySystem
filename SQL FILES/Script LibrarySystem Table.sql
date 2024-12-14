-- Create the Users table
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    user_address VARCHAR(255),
    email_address VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(15)
);

-- Create the Books table
CREATE TABLE Books (
    isbn VARCHAR(13) PRIMARY KEY,
    book_title VARCHAR(255) NOT NULL,
    date_of_publication DATE
);

-- Create the Authors table
CREATE TABLE Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_firstname VARCHAR(255) NOT NULL,
    author_surname VARCHAR(255) NOT NULL
);

-- Create the Books_Authors junction table (to resolve M:N relationship between Books and Authors)
CREATE TABLE Books_Authors (
    book_author_id INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13) NOT NULL,
    author_id INT NOT NULL,
    FOREIGN KEY (isbn) REFERENCES Books(isbn) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id) ON DELETE CASCADE
);

-- Create the Categories table
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL UNIQUE
);

-- Add a foreign key in the Books table to reference Categories
ALTER TABLE Books
ADD category_id INT,
ADD FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE SET NULL;

-- Create the Loans table
CREATE TABLE Loans (
    book_borrowing_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    isbn VARCHAR(13) NOT NULL,
    date_issued DATE NOT NULL,
    date_due_for_return DATE NOT NULL,
    date_returned DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (isbn) REFERENCES Books(isbn) ON DELETE CASCADE
);

-- Create the Library Rules table (optional)
CREATE TABLE Library_Rules (
    rule_id INT AUTO_INCREMENT PRIMARY KEY,
    rule_description VARCHAR(255) NOT NULL,
    rule_value DECIMAL(10, 2) NOT NULL
);
