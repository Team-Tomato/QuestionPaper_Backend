import os
import json
import flask
import requests
import psycopg2
from flask import request
from waitress import serve
from databaseScripts.searchQueries import *
from flask_restful import reqparse, Api, Resource


# Initialize the App
app = flask.Flask(__name__)
app.config.from_json(os.path.join(os.path.abspath(os.getcwd()),'config/productionConfig.json'))
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


api.add_resource(questionPaper, '/api/v1/teamtomato/')


if __name__ == "__main__":
    # app.run()
    serve(app, port=4950)
