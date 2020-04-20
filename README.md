# web-app-Question-paper
Flask API serves questionpaper URL from the drive repository.

### Postman Collection : https://www.getpostman.com/collections/63a0dfc9ae6d2657ee29

### Deployed in heroku : https://teamtomato.herokuapp.com

### Setup for development
1. clone the repo to your local
``` 
git clone https://github.com/Team-Tomato/QuestionPaper_Backend.git
```
2. Install the dependencies
```
pip install requirements.txt
```
3. Add or modify the **.env** file according to your local postgres database. Here is the example **.env** file. Leave the APP_SETTINGS as it is.
```
APP_SETTINGS="config.DevelopmentConfig"
POSTGRES_URL="127.0.0.1:5432"
POSTGRES_USER="postgres"
POSTGRES_PW="password"
POSTGRES_DB="db-name"
```
4. Create the database in your local with your database name "db-name" adn start your local database server.
5. Run the following commands to mirate the database.
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
6. Start the server,
```
python manage.py runserver
```
7. Try hitting the end points for sample testing.

**Note:**
If your changes adds some dependencies to the system, kindly update the requirements.txt file using pipreqs
```
pipreqs /path/to/project/QuestionPaper_Backend --force
```
