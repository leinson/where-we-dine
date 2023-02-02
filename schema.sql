CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT, 
    admin BOOLEAN
);

CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY, 
    name TEXT UNIQUE, 
    info TEXT, 
    web_link TEXT, 
    city TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY, 
    restaurant_id INTEGER REFERENCES restaurants ON DELETE CASCADE, 
    user_id INTEGER REFERENCES users ON DELETE CASCADE, 
    review TEXT,
    score INTEGER, 
    visited DATE, 
    sent_at TIMESTAMP
);