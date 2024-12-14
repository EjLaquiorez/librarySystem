-- Insert sample data into users
INSERT INTO users (user_name, user_address, email_address, phone_number) VALUES
('Juan Dela Cruz', '123 Mabini St, Manila', 'juan.delacruz1@example.com', '09171234567'),
('Maria Santos', '456 Rizal Ave, Quezon City', 'maria.santos2@example.com', '09181234567'),
('Jose Rizal', '789 Bonifacio St, Cebu', 'jose.rizal3@example.com', '09191234567'),
('Andres Bonifacio', '321 Aguinaldo St, Davao', 'andres.bonifacio4@example.com', '09201234567'),
('Emilio Aguinaldo', '654 Maginhawa St, Pasig', 'emilio.aguinaldo5@example.com', '09211234567'),
('Melchora Aquino', '987 Heroes St, Makati', 'melchora.aquino6@example.com', '09221234567'),
('Gabriela Silang', '123 Freedom St, Taguig', 'gabriela.silang7@example.com', '09231234567'),
('Apolinario Mabini', '456 Revolution Rd, Baguio', 'apolinario.mabini8@example.com', '09241234567'),
('Lapu-Lapu', '789 Victory Lane, Iloilo', 'lapu.lapu9@example.com', '09251234567'),
('Diego Silang', '321 Courage St, Bacolod', 'diego.silang10@example.com', '09261234567'),
('Heneral Luna', '654 Independence Ave, Zamboanga', 'heneral.luna11@example.com', '09271234567'),
('Antonio Luna', '987 Rizal Blvd, Cavite', 'antonio.luna12@example.com', '09281234567'),
('Gregorio Del Pilar', '123 Patriot St, Pampanga', 'gregorio.pilar13@example.com', '09291234567'),
('Manuel Quezon', '456 Commonwealth Ave, Bulacan', 'manuel.quezon14@example.com', '09301234567'),
('Sergio Osmena', '789 Legacy St, Leyte', 'sergio.osmena15@example.com', '09311234567'),
('Carlos P. Romulo', '321 United Nations Rd, Pasay', 'carlos.romulo16@example.com', '09321234567'),
('Francisco Balagtas', '654 Poet St, Batangas', 'francisco.balagtas17@example.com', '09331234567'),
('Josefa Llanes Escoda', '987 Womens St, La Union', 'josefa.escoda18@example.com', '09341234567'),
('Marcelo H. Del Pilar', '123 La Solidaridad Rd, Tarlac', 'marcelo.pilar19@example.com', '09351234567'),
('Leona Florentino', '456 Literature St, Ilocos', 'leona.florentino20@example.com', '09361234567'),
('Trinidad Tecson', '789 Brave St, Laguna', 'trinidad.tecson21@example.com', '09371234567'),
('Ramon Magsaysay', '321 Service St, Nueva Ecija', 'ramon.magsaysay22@example.com', '09381234567'),
('Corazon Aquino', '654 Democracy St, Pangasinan', 'corazon.aquino23@example.com', '09391234567'),
('Benigno Aquino Jr.', '987 Justice St, Samar', 'benigno.aquino24@example.com', '09401234567'),
('Ferdinand Marcos', '123 Maharlika St, Ilocos Norte', 'ferdinand.marcos25@example.com', '09411234567'),
('Jose Abad Santos', '456 Honor St, Surigao', 'jose.santos26@example.com', '09421234567'),
('Vicente Sotto', '789 Press Freedom Rd, Cebu', 'vicente.sotto27@example.com', '09431234567'),
('Elpidio Quirino', '321 Rehabilitation St, Vigan', 'elpidio.quirino28@example.com', '09441234567'),
('Manuel Roxas', '654 Reconstruction St, Capiz', 'manuel.roxas29@example.com', '09451234567'),
('Emilio Jacinto', '987 Sublime St, Marikina', 'emilio.jacinto30@example.com', '09461234567');


-- Insert sample data into books
INSERT INTO books (isbn, book_title, date_of_publication) VALUES
('9781234567897', 'Noli Me Tangere', '1887-10-10'),
('9782345678901', 'El Filibusterismo', '1891-09-18'),
('9783456789012', 'Florante at Laura', '1838-01-01'),
('9784567890123', 'Mga Kwento ni Lola Basyang', '1925-06-01'),
('9785678901234', 'Banaag at Sikat', '1906-01-01');

-- Insert sample data into authors
INSERT INTO authors (author_firstname, author_surname) VALUES
('Jose', 'Rizal'),
('Francisco', 'Balagtas'),
('Severino', 'Reyes'),
('Lope', 'Santos'),
('Lualhati', 'Bautista');

-- Insert sample data into books_authors
INSERT INTO books_authors (isbn, author_id) VALUES
('9781234567897', 1),
('9782345678901', 1),
('9783456789012', 2),
('9784567890123', 3),
('9785678901234', 4);

-- Insert sample data into categories
INSERT INTO categories (category_id, category_name) VALUES 
(1, 'fiction'),
(2, 'historical fiction'),
(3, 'poetry'),
(4, 'children''s literature');

-- Update books to assign categories
UPDATE books SET category_id = 2 WHERE isbn = '9781234567897';
UPDATE books SET category_id = 2 WHERE isbn = '9782345678901';
UPDATE books SET category_id = 3 WHERE isbn = '9783456789012';
UPDATE books SET category_id = 4 WHERE isbn = '9784567890123';
UPDATE books SET category_id = 1 WHERE isbn = '9785678901234';

-- Insert sample data into loans
INSERT INTO loans (user_id, isbn, date_issued, date_due_for_return, date_returned) VALUES
(1, '9781234567897', '2024-11-01', '2024-11-15', '2024-11-14'),
(2, '9782345678901', '2024-11-02', '2024-11-16', NULL);

-- Insert sample data into library_rules
INSERT INTO library_rules (rule_description, rule_value) VALUES
('overdue fine (per day)', 10.00),
('maximum books per user', 5),
('loan period (days)', 14);
