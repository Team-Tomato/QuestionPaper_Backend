import os
import json
import flask
import requests
import psycopg2
from flask import request,jsonify
from waitress import serve
from databaseScripts.searchQueries import *
from flask_restful import reqparse, Api, Resource

#An Array of key:value pairs
questionPapers=[
{
    "Course Code":"XC7351",
    "Course Title":"Data Structures",
    "Year":"2019"
},
{
    "Course Code":"XC7352",
    "Course Title":"Database Management Systems",
    "Year":"2019"
}
]

# Initialize the App
app = flask.Flask(__name__)
#Dev environment    - config/config.json
#Prod environement  - config/productionConfig.json
app.config.from_json(os.path.join(os.path.abspath(os.getcwd()),'config/config.json'))
api = Api(app)


# Parsable arguments
parser = reqparse.RequestParser()
parser.add_argument('keyword')


def getDbConnection():
    dbConnection = psycopg2.connect(   user = app.config["DATABASE"]["USERNAME"],
                                    password = app.config["DATABASE"]["PASSWORD"],
                                    host = app.config["DATABASE"]["HOSTNAME"],
                                    port = app.config["DATABASE"]["PORT"],
                                    database = app.config["DATABASE"]["DATABASENAME"] )
    return [dbConnection, dbConnection.cursor()]

def closeDbConnection(connection, cursor):
    if(connection):
        cursor.close()
        connection.close()


# API - 01
class questionPaper(Resource):
    def post(self):
        DbConnection, cursor = getDbConnection()

        args = parser.parse_args()
        keyword = args['keyword']
        urlArray = []

        try:
            cursor.execute(returnSubjectName,(keyword,) )
            urlArray = urlArray + cursor.fetchall()
            cursor.execute(returnShortForm,(keyword,) )
            urlArray = urlArray + cursor.fetchall()
            cursor.execute(returnStaff,(keyword,) )
            urlArray = urlArray + cursor.fetchall()
            return {    "success": True,
                        "message": "Question papers fetched successfully",
                        "data": urlArray    }
        

        except (Exception, psycopg2.Error) as error :
            return {    "success": False,
                        "message": str(error),
                        "data": "Failed"    }
        finally:
            closeDbConnection(DbConnection, cursor)


class TeamTomato(Resource):
    def get(self):
        return "Team Tomato welcomes you"

class List(Resource):
    def get(self):
        return jsonify(questionPapers)

class addToList(Resource):
    def post(self):
        new_subject=request.get_json()
        questionPapers.append(new_subject)
        return jsonify(questionPapers)


api.add_resource(questionPaper, '/api/v1/teamtomato/')
api.add_resource(TeamTomato, '/')
api.add_resource(List,'/listQPS')
api.add_resource(addToList,'/addQP')


if __name__ == "__main__":
    # app.run()
    # serve(app, port=(process.env.PORT or 4950))
    serve(app)
