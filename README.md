# where-we-dine

- A restaurant review app
- Created for the Database application study project (Tietokantasovellus harjoitustyö) at University of Helsinki

 
## How to use
- Fly.io link: https://where-we-dine.fly.dev/
- For testing admin features: 
    - username: admintest, password: test123 
  
- Refresh the page if you get "Internal server error" when you open the link
- If fly.io for some other reason does not work, you can test the application locally on your computer. Instructions are at the bottom of the README.
### Features

- Eliminate vulnerabilities (csrf)
- A user can search for a restaurant based on cuisine
- A user can organize the list of restaurants based on the review scores

### Välipalautus 3 :

- Admin can in the app add new cuisine types and delete them
- Admin can add types of cuisines to a new restaurant
- Admin can add the price range to a new restaurant
- Separate user page that displays the users written reviews
- Delete own reviews from user page
- Delete own account (except admins)
- fly.io deployment


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


## To Do

### Page and account management
- Admin right to remove any restaurant 

### Organizing and search features 
- A user can search for a restaurant based on price or restaurant name

 
### Other stuff
- Make visually pleasing, add own CSS or Bootstrap library (in progress)
- Move cuisine functions to own file
- check pylint


### Future development ideas
- A user can add a restaurant without info & tags 
    - An admin can later "verify" the restaurant, and add the info & tags 
- A user can edit their own review after it is posted 
- A user can do a list of restaurants they want to visit 
- A user can add pictures to their review
- Admin can edit restaurant info

## How to run on your own computer
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
