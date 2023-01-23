# where-we-dine

- A restaurant review app
- Created for the Database application study project at University of Helsinki


## Early stage ideas for what will be included in the program

### Main functionalities

- A view, which shows all added restaurants 

- When clicking on a restaurant, the restaurants information and reviews show 

- A user can add a review to an existing restaurant 

    - Write a review 

    - Add date of visit 

    - Choose a score 

    - Add available tags 

- An admin can add a new restaurant to the page 

    - Add restaurants name 

    - Write information about the restaurant 

    - Link to the restaurant’s webpage 

    - City 

    - Add cuisine and price tags 


### Page and account management

- Create an account, normal user or admin 

- Log in and out 

- User page, where the user can 

    - See their own reviews 

    - Remove own reviews 

    - Remove own account 

- Admin right to remove anyone’s review, account, or any restaurant 

 

### Organizing and search features 

- An admin can create tags that belong to the categories cuisine and price 

- A user can search for a restaurant based on a tag or restaurant name

- A user can organize the list of restaurants based on the review scores 

 

### “Nice to have’s”

- A user can add a restaurant by themselves, without info & tags 

    - An admin can later add the info & tags 

- A user can edit their own review after it is posted 

- A user can do a list of restaurants they want to visit 

 
## How to install (in progress)

- Clone repository to your computer
- Install virtual enviroment into the project folder: python3 -m venv venv
- Go to virtual environment: $ source venv/bin/activate
- Install requirements: pip install -r requirements.txt
- Add file: .env , add to it:DATABASE_URL=postgresql+psycopg2:///yourusername . Also add a SECRET_KEY ?
- change to your username in db.py
- Install postgresql (https://hy-tsoha.github.io/materiaali/osa-2/#tietokannan-k%C3%A4ytt%C3%A4minen)
- Open start-pg.sh in another terminal - keep open
- Run app: flask run