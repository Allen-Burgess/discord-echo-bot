CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    nickname VARCHAR(255) UNIQUE,
    description VARCHAR(255)
);

CREATE TABLE quotes (
    id INT PRIMARY KEY,
    quote_text VARCHAR(255),
    user_id INT,
    timestamp INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
