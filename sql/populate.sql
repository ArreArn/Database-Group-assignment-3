-- ---------------------------
-- 1. PUBLISHER
-- ---------------------------
INSERT INTO publisher (name, address, phone, email)
VALUES
    ('Penguin Random House', '1745 Broadway, New York, NY 10019', '212-555-1001', 'contact@penguinrandomhouse.com'),
    ('HarperCollins', '195 Broadway, New York, NY 10007', '212-555-1002', 'info@harpercollins.com'),
    ('Simon & Schuster', '1230 Avenue of the Americas, New York, NY 10020', '212-555-1003', 'inquiries@simonandschuster.com'),
    ('Macmillan', '120 Broadway, New York, NY 10271', '212-555-1004', 'help@macmillan.com'),
    ('Hachette Book Group', '1290 Avenue of the Americas, New York, NY 10104', '212-555-1005', 'support@hachettebookgroup.com'),
    ('Scholastic', '557 Broadway, New York, NY 10012', '212-555-1006', 'hello@scholastic.com'),
    ('Oxford University Press', '198 Madison Ave, New York, NY 10016', '212-555-1007', 'info@oup.com'),
    ('Cambridge University Press', '1 Liberty Plaza, Floor 20, New York, NY 10006', '212-555-1008', 'inquiries@cambridge.org'),
    ('Wiley', '111 River St, Hoboken, NJ 07030', '212-555-1009', 'contact@wiley.com'),
    ('Pearson', '221 River St, Hoboken, NJ 07030', '212-555-1010', 'support@pearson.com');

-- ---------------------------
-- 2. BOOK
-- ---------------------------
-- Each book references a valid publisher_id (1 through 10).
INSERT INTO book (title, author, publisher_id, isbn, year_published)
VALUES
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1, '978-0743273565', 1925),
    ('To Kill a Mockingbird', 'Harper Lee', 2, '978-0060935467', 1960),
    ('1984', 'George Orwell', 3, '978-0451524935', 1949),
    ('Pride and Prejudice', 'Jane Austen', 4, '978-1503290563', 1813),
    ('Moby-Dick', 'Herman Melville', 5, '978-0142437247', 1851),
    ('War and Peace', 'Leo Tolstoy', 6, '978-0199232765', 1869),
    ('The Catcher in the Rye', 'J.D. Salinger', 7, '978-0316769488', 1951),
    ('Brave New World', 'Aldous Huxley', 8, '978-0060850524', 1932),
    ('Crime and Punishment', 'Fyodor Dostoevsky', 9, '978-0143058144', 1866),
    ('Jane Eyre', 'Charlotte Brontë', 10, '978-0142437209', 1847);

-- ---------------------------
-- 3. MEMBER
-- ---------------------------
-- Each member has a unique date_of_membership and required fields.
INSERT INTO member (first_name, last_name, email, phone, address, date_of_membership)
VALUES
    ('John', 'Doe', 'john.doe@example.com', '555-0001', '123 Elm Street', '2020-01-15'),
    ('Jane', 'Smith', 'jane.smith@example.com', '555-0002', '456 Oak Avenue', '2021-03-10'),
    ('Michael', 'Johnson', 'michael.johnson@example.com', '555-0003', '789 Pine Road', '2019-11-23'),
    ('Emily', 'Davis', 'emily.davis@example.com', '555-0004', '321 Maple Lane', '2022-05-05'),
    ('William', 'Brown', 'william.brown@example.com', '555-0005', '654 Walnut Street', '2020-07-17'),
    ('Olivia', 'Taylor', 'olivia.taylor@example.com', '555-0006', '987 Cedar Avenue', '2021-12-01'),
    ('James', 'Anderson', 'james.anderson@example.com', '555-0007', '159 Spruce Road', '2022-02-14'),
    ('Sophia', 'Thomas', 'sophia.thomas@example.com', '555-0008', '753 Birch Boulevard', '2018-09-29'),
    ('Daniel', 'Jackson', 'daniel.jackson@example.com', '555-0009', '357 Pine Crescent', '2019-08-08'),
    ('Ava', 'Martinez', 'ava.martinez@example.com', '555-0010', '159 Cherry Street', '2023-01-01');

-- ---------------------------
-- 4. STAFF
-- ---------------------------
-- Each staff has a role (e.g., 'Librarian', 'Assistant', 'Manager', etc.).
INSERT INTO staff (first_name, last_name, email, phone, role)
VALUES
    ('Alice', 'Smith', 'alice.smith@library.com', '555-1001', 'Librarian'),
    ('Bob', 'Johnson', 'bob.johnson@library.com', '555-1002', 'Assistant'),
    ('Charlie', 'Williams', 'charlie.williams@library.com', '555-1003', 'Manager'),
    ('Diana', 'Brown', 'diana.brown@library.com', '555-1004', 'Librarian'),
    ('Ethan', 'Jones', 'ethan.jones@library.com', '555-1005', 'IT Support'),
    ('Fiona', 'Garcia', 'fiona.garcia@library.com', '555-1006', 'Clerk'),
    ('George', 'Miller', 'george.miller@library.com', '555-1007', 'Librarian'),
    ('Hannah', 'Davis', 'hannah.davis@library.com', '555-1008', 'Assistant'),
    ('Ivan', 'Rodriguez', 'ivan.rodriguez@library.com', '555-1009', 'Manager'),
    ('Julia', 'Wilson', 'julia.wilson@library.com', '555-1010', 'Clerk');

-- ---------------------------
-- 5. LOAN
-- ---------------------------
-- Must reference valid book_id (1-10), member_id (1-10), and staff_id (1-10).
-- date_returned can be NULL or set if returned.
INSERT INTO loan (book_id, member_id, staff_id, date_borrowed, due_date, date_returned)
VALUES
    (1, 1, 1, '2023-01-01', '2023-01-15', '2023-01-12'),    -- Returned
    (2, 2, 2, '2023-01-05', '2023-01-20', NULL),           -- Not returned yet
    (3, 3, 3, '2023-02-10', '2023-02-24', '2023-02-23'),
    (4, 4, 4, '2023-03-01', '2023-03-15', '2023-03-14'),
    (5, 5, 5, '2023-03-10', '2023-03-25', NULL),
    (6, 6, 6, '2023-04-01', '2023-04-15', '2023-04-13'),
    (7, 7, 7, '2023-05-05', '2023-05-20', NULL),
    (8, 8, 8, '2023-05-15', '2023-05-30', '2023-05-29'),
    (9, 9, 9, '2023-06-01', '2023-06-15', NULL),
    (10, 10, 10, '2023-06-10', '2023-06-25', '2023-06-24');
