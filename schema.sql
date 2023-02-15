CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT, 
    admin BOOLEAN
);

CREATE TABLE IF NOT EXISTS restaurants (
    id SERIAL PRIMARY KEY, 
    name TEXT UNIQUE, 
    info TEXT, 
    web_link TEXT, 
    city TEXT,
    price TEXT
);

CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY, 
    restaurant_id INTEGER REFERENCES restaurants ON DELETE CASCADE, 
    user_id INTEGER REFERENCES users ON DELETE CASCADE, 
    review TEXT,
    score INTEGER, 
    visited DATE, 
    sent_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cuisines (
    id SERIAL PRIMARY KEY, 
    cuisine TEXT
);

CREATE TABLE IF NOT EXISTS restaurant_cuisines (
    restaurant_id INTEGER REFERENCES restaurants ON DELETE CASCADE,
    cuisine_id INTEGER REFERENCES cuisines ON DELETE CASCADE
);
