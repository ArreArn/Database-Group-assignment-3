CREATE TABLE IF NOT EXISTS publisher (
    publisher_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    publisher_id INTEGER,
    isbn VARCHAR(20),
    year_published INTEGER,
    FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id)
    ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS member (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(255),
    date_of_membership DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    role VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS loan (
    loan_id SERIAL PRIMARY KEY,
    book_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    date_borrowed DATE NOT NULL,
    due_date DATE NOT NULL,
    date_returned DATE,
    FOREIGN KEY (book_id) REFERENCES book(book_id)
    ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES member(member_id)
    ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
    ON DELETE SET NULL
);
