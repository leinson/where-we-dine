# where-we-dine

- A restaurant review app
- Created for the Database application study project (Tietokantasovellus harjoitustyö) at University of Helsinki


### Välipalautus 3 :
- Admin can add types of cuisines to a new restaurant, aka can create cuisine tags
- Add price range to a restaurant

To do:

- user page & remove options
- fly.io

### Välipalautus 2 : 

- A view, which shows all added restaurants 

- When clicking on a restaurant, the restaurants information and reviews show 

- A user can add a review to an existing restaurant 

    - Write a review 
    - Add date of visit 
    - Choose a score 

- An admin can add a new restaurant to the page 

    - Add restaurants name 
    - Write information about the restaurant 
    - Link to the restaurant’s webpage 
    - City 
 
- Create an account, normal user (or admin)
    - Admin rights manually added to database

- Log in and out 

- Restrictments in html and python to block invalid inputs
 
## How to install
Fly.io deployment not yet in use. You can test the application locally on your computer:

- Clone repository to your computer
- Add file: .env and add to it: 
    - DATABASE_URL=postgresql+psycopg2:///yourusername  
    - SECRET_KEY=a-secret-key
- Install virtual enviroment into the project folder: python3 -m venv venv
- Go to virtual environment: $ source venv/bin/activate
- Install requirements: pip install -r requirements.txt

- change to your username in db.py if needed
- (Install postgresql https://hy-tsoha.github.io/materiaali/osa-2/#tietokannan-k%C3%A4ytt%C3%A4minen)
- add database: psql < schema.sql
- add an admin user and a couple of restaurants for testing: psql < queries.sql
    - if this doesn't work, you can manually in psql change your user to an admin by changing the admin column to 'true'
- Open :start-pg.sh , in another terminal - keep open
- Run app: flask run


- Will try to get fly.io deployment to Välipalautus 3.

## To Do

### Features
- Admin can:
    - Can edit all info about a restaurant afterwards
    - Add price range to a restaurant

### Page and account management

- User page, where the user can 
    - See their own reviews 
    - Remove own reviews 
    - Remove own account 

- Admin right to remove anyone’s review, account, or any restaurant 
 

### Organizing and search features 

- A user can search for a restaurant based on cuisine, price or restaurant name

- A user can organize the list of restaurants based on the review scores 
 

### “Nice to have’s”

- A user can add a restaurant without info & tags 

    - An admin can later "verify" the restaurant, and add the info & tags 

- A user can edit their own review after it is posted 

- A user can do a list of restaurants they want to visit 

- A user can add pictures to their review
