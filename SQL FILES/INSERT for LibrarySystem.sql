
-- Insert sample data into Users
INSERT INTO Users (user_name, user_address, email_address, phone_number) VALUES
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


-- Insert sample data into Books
INSERT INTO Books (isbn, book_title, date_of_publication) VALUES
('9781234567897', 'Noli Me Tangere', '1887-10-10'),
('9782345678901', 'El Filibusterismo', '1891-09-18'),
('9783456789012', 'Florante at Laura', '1838-01-01'),
('9784567890123', 'Mga Kwento ni Lola Basyang', '1925-06-01'),
('9785678901234', 'Banaag at Sikat', '1906-01-01'),
('9786789012345', 'Dekada 70', '1983-01-01'),
('9787890123456', 'Gapo', '1988-01-01'),
('9788901234567', 'Hibik ng Pilipinas', '1896-01-01'),
('9789012345678', 'Makabayan', '1922-01-01'),
('9780123456789', 'Ibong Adarna', '1600-01-01'),
('9782233445566', 'Tagalog Love Stories', '1950-01-01'),
('9783344556677', 'Pag-ibig sa Bayan', '1940-01-01'),
('9784455667788', 'Dugo at Pawis', '1931-01-01'),
('9785566778899', 'Buhay Pilipino', '1929-01-01'),
('9786677889900', 'Mga Anak Dalita', '1911-01-01'),
('9787788990011', 'Alamat ng Gubat', '2003-01-01'),
('9788899001122', 'ABNKKBSNPLAko?!', '2001-01-01'),
('9789900112233', 'Laro sa Baga', '1999-01-01'),
('9781011123344', 'Ang Larawan', '1949-01-01'),
('9781112233445', 'Kuwadro sa Dilim', '1952-01-01'),
('9782223344556', 'Biyaya ng Langit', '1930-01-01'),
('9783334455667', 'Kwento ng Buhay', '1943-01-01'),
('9784445566778', 'Ang Bahaghari', '1923-01-01'),
('9785556677889', 'Pagsubok sa Bayan', '1908-01-01'),
('9786667788990', 'Sa Piling ng Bituin', '1915-01-01'),
('9787778899001', 'Tagumpay ng Bayan', '1898-01-01'),
('9788889900112', 'Pagdiriwang ng Kalayaan', '1907-01-01'),
('9789990011223', 'Pananampalataya', '1905-01-01'),
('9780001122334', 'Ang Wika ng Bayan', '1914-01-01'),
('9780011223344', 'Mga Lihim ng Tahanan', '1927-01-01');




-- Insert sample data into Authors
INSERT INTO Authors (author_firstname, author_surname) VALUES
('Jose', 'Rizal'),
('Francisco', 'Balagtas'),
('Severino', 'Reyes'),
('Lope', 'Santos'),
('Lualhati', 'Bautista'),
('Carlos', 'Bulosan'),
('Emilio', 'Jacinto'),
('Andres', 'Bonifacio'),
('Jose', 'García Villa'),
('Bob', 'Ong'),
('Nick', 'Joaquin'),
('F. Sionil', 'Jose'),
('Amado', 'V. Hernandez'),
('Alejandro', 'Roces'),
('N.V.M.', 'Gonzalez'),
('Bienvenido', 'Santos'),
('Virgilio', 'Almario'),
('Edgardo', 'Reyes'),
('Jessica', 'Zafra'),
('Ricardo', 'Lee'),
('Cristina', 'Pantoja-Hidalgo'),
('Ambeth', 'Ocampo'),
('Rogelio', 'Ordoñez'),
('Genoveva', 'Matute'),
('Estrella', 'Alfon'),
('Danton', 'Remoto'),
('Manuel', 'Arguelles'),
('Lamberto', 'Avellana'),
('Manuel', 'Quezon III'),
('Teodoro', 'Agoncillo');

-- Insert sample data into Books_Authors
INSERT INTO Books_Authors (isbn, author_id) VALUES
('9781234567897', 1), -- Noli Me Tangere by Jose Rizal
('9782345678901', 1), -- El Filibusterismo by Jose Rizal
('9783456789012', 2), -- Florante at Laura by Francisco Balagtas
('9784567890123', 3), -- Mga Kwento ni Lola Basyang by Severino Reyes
('9785678901234', 4), -- Banaag at Sikat by Lope Santos
('9786789012345', 5), -- Dekada '70 by Lualhati Bautista
('9787890123456', 6), -- Gapo by Carlos Bulosan
('9788901234567', 7), -- Hibik ng Pilipinas by Emilio Jacinto
('9789012345678', 8), -- Makabayan by Andres Bonifacio
('9780123456789', 9), -- Ibong Adarna (unknown author)
('9782233445566', 10), -- Tagalog Love Stories by Bob Ong
('9783344556677', 11), -- Pag-ibig sa Bayan by Nick Joaquin
('9784455667788', 12), -- Dugo at Pawis by F. Sionil Jose
('9785566778899', 13), -- Buhay Pilipino by Amado V. Hernandez
('9786677889900', 14), -- Mga Anak Dalita by Alejandro Roces
('9787788990011', 15), -- Alamat ng Gubat by N.V.M. Gonzalez
('9788899001122', 10), -- ABNKKBSNPLAko?! by Bob Ong
('9789900112233', 16), -- Laro sa Baga by Bienvenido Santos
('9781011123344', 17), -- Ang Larawan by Virgilio Almario
('9781112233445', 18); -- Kuwadro sa Dilim by Edgardo Reyes

-- Insert sample data into Categories
INSERT INTO Categories (category_id, category_name) VALUES 
(1, 'Fiction'),
(2, 'Historical Fiction'),
(3, 'Poetry'),
(4, 'Children\'s Literature'), -- Replaced curly apostrophe
(5, 'Romance'),
(6, 'Drama'),
(7, 'Classic Literature'),
(8, 'Essays'),
(9, 'Biography'),
(10, 'Science Fiction'),
(11, 'Mystery'),
(12, 'Philosophy'),
(13, 'Politics'),
(14, 'Fantasy'),
(15, 'Horror');

-- Update Books to assign Categories
UPDATE Books SET category_id = 2 WHERE isbn = '9781234567897'; -- Historical Fiction for Noli Me Tangere
UPDATE Books SET category_id = 2 WHERE isbn = '9782345678901'; -- Historical Fiction for El Filibusterismo
UPDATE Books SET category_id = 3 WHERE isbn = '9783456789012'; -- Poetry for Florante at Laura
UPDATE Books SET category_id = 4 WHERE isbn = '9784567890123'; -- Children’s Literature for Lola Basyang
UPDATE Books SET category_id = 1 WHERE isbn = '9785678901234'; -- Fiction for Banaag at Sikat

-- Insert sample data into Loans
INSERT INTO Loans (user_id, isbn, date_issued, date_due_for_return, date_returned) VALUES
(1, '9781234567897', '2024-11-01', '2024-11-15', '2024-11-14'),
(2, '9782345678901', '2024-11-02', '2024-11-16', NULL), -- Not yet returned
(3, '9783456789012', '2024-11-03', '2024-11-17', '2024-11-17'),
(4, '9784567890123', '2024-11-05', '2024-11-19', NULL), -- Not yet returned
(5, '9785678901234', '2024-11-07', '2024-11-21', '2024-11-20'),
(6, '9786789012345', '2024-11-08', '2024-11-22', NULL),
(7, '9787890123456', '2024-11-10', '2024-11-24', NULL),
(8, '9788901234567', '2024-11-11', '2024-11-25', '2024-11-24');

-- Insert sample data into Library_Rules
INSERT INTO Library_Rules (rule_description, rule_value) VALUES
('Overdue Fine (Per Day)', 10.00),
('Maximum Books Per User', 5),
('Loan Period (Days)', 14);
