# web-app-Question-paper
Flask API serves questionpaper URL from the drive repository.

### API
##### API 01 - questionPaper
host:port/api/v1/teamtomato/
```json
Response:   {
                "success": ,
                "message": ,
                "data": []
            }
```

##### API 02 - TestApi(TeamTomato)
host:port/
```
Team Tomato welcomes you
```

### Setup for development
1. clone the repo to your local
``` 
git clone https://github.com/Team-Tomato/QuestionPaper_Backend.git
```
2. Install the dependencies
```
pip install requirements.txt
```
3. Change the **config/config.json** file according to your local postgres database
4. Create the database in your local and execute the db initialisation scripts available in the databaseScripts/dbInitialisation.sql
5. For development environment, ensure Line 16 in app.py was set to config/config.json
6. Start the server,
```
python app.py
```
7. Try hitting the end points for sample testing.

**Note:**
If your changes adds some dependencies to the system, kindly update the requirements.txt file using pipreqs
```
pipreqs /path/to/project/QuestionPaper_Backend --force
```
