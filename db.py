from os import getenv
from flask_sqlalchemy import SQLAlchemy
from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Examples of queries done now straight to the database
# INSERT INTO restaurants (name, info, web_link, city) VALUES ('Goose Pastabar', 'Korttelikuppila, jossa tarjotaan itsetehtyä pastaa.', 'https://www.goosepastabar.com/', 'Helsinki')
# INSERT INTO users (username, password, admin) VALUES ('testuser', 'test123', 'false')

# INSERT INTO reviews (restaurant_id, user_id, review, score, visited, sent_at) VALUES (1, 1, 'Erittäin hyvää pastaa', 10, '2023-01-18', LOCALTIMESTAMP(0));
