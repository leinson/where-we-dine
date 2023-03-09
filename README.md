# where-we-dine

- A restaurant review app
- Created for the Database application study project (Tietokantasovellus harjoitustyö) at University of Helsinki
 
## How to use
- Deployed at https://where-we-dine.fly.dev/
- For testing Admin features: 
    - username: `admintest`
    - password: `test123`
- Refresh the page if you get "Internal server error" when you open the link
- If fly.io for some other reason does not work, you can test the application locally on your computer. Instructions are at the bottom of the README.
- /9.3.2023 **NOTE:** After the deadline, I noticed that the search functionality filters that work perfectly on my computer, does not work without logging in on other computers/devices. To test the functionality, please log in/register. (The problem is probably in the added CSRF check, since the search function without loging works after one "log in - log out"). I will update this to a functioning version after this project is scored and reviewed.

## Features 

**Visitor:**
- A view, which shows all added restaurants 
- When clicking on a restaurant, the restaurants information and reviews show 
- Sort restaurants by average score, price and cuisine tags
- Create an account

**Registered user:**
- A user can add a review to an existing restaurant 
    - Write a review 
    - Add date of visit  
    - Choose a score 
- Log in and out
- User page:
    - See their own reviews
    - Delete account (except admins)
    - Remove their own reviews

**Admin:**
- Add a new restaurant to the page 
    - Restaurants name 
    - Write information about the restaurant 
    - Link to the restaurant’s webpage 
    - Add cuisines
    - Add price
    - City 
- Add cuisine tags and delete them
- Remove anyones review
- Right to access anyones profile by changing the url to another users id

### For future development
- A user can add a restaurant without info & tags 
- A user can edit their own review after it is posted 
- A user can do a list of restaurants they want to visit 
- A user can add pictures to their review
- Admin can edit restaurant info in app
- Admin can remove restaurants in app
- Search bar for free word search

## How to use locally
- Clone repository to your computer
- Add file: `.env` and add to it: 
    - `DATABASE_URL=postgresql+psycopg2:///yourusername`
    - `SECRET_KEY=a-secret-key`
- Install virtual enviroment into the project folder: `python3 -m venv venv`
- Go to virtual environment: `source venv/bin/activate`
- Install requirements: `pip install -r requirements.txt`

- Change to your username in db.py if needed
- (Install postgresql if needed: https://hy-tsoha.github.io/materiaali/osa-2/#tietokannan-k%C3%A4ytt%C3%A4minen)
- Add database: `psql < schema.sql`
- Add an admin user and a couple of restaurants for testing: `psql < queries.sql`
    - if this doesn't work, you can manually in psql change your user to an admin by changing the admin column to 'true'
- Open: `start-pg.sh` , in another terminal - keep open
- Run app: `flask run`
