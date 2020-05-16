# web-app-Question-paper
Flask API serves questionpaper URL from the drive repository.

### Postman Collection : https://www.getpostman.com/collections/63a0dfc9ae6d2657ee29

### Deployed in heroku : https://teamtomato.herokuapp.com

### Setup for development
1. Clone the repo to your local
``` 
git clone https://github.com/Team-Tomato/QuestionPaper_Backend.git
```
2. Create or Activate your vitrual environment.
```
virtualenv env
source env/bin/activate
```
3. Install the dependencies from **requirements.txt**
```
pip install -r requirements.txt
```
4. Add or modify the **.env** file according to your local postgres database. Here is the example **.env** file. Leave the APP_SETTINGS,EMAIL_USER,EMAIL_PASSWORD as it is 
```
APP_SETTINGS="config.DevelopmentConfig"
POSTGRES_URL="127.0.0.1:5432"
POSTGRES_USER="postgres"
POSTGRES_PW="password"
POSTGRES_DB="db-name"
EMAIL_USER="email_id"
EMAIL_PASSWORD="email_password"
USER_NAME="Team-Tomato"
```
5. Create the database in your local with your database name **db-name** adn start your local database server.
6. Run the following commands to mirate the database.
```
python manage.py db init            #If prompts error, leave it.
python manage.py db migrate
python manage.py db upgrade
```
7. Start the server,
```
python manage.py runserver
```
8. Try hitting the end points for sample testing.

**Note:**
If your changes adds some dependencies to the system, kindly update the requirements.txt file using pipreqs
```
pipreqs /path/to/project/QuestionPaper_Backend --force
```
