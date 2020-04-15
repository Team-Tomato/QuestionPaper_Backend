import os
import json
import flask
import requests
import psycopg2
from flask import request,jsonify
from waitress import serve
from databaseScripts.searchQueries import *
from flask_restful import reqparse, Api, Resource

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

def getDbConnectionVK():
    dbConnection = psycopg2.connect( user = app.config["DATABASEVK"]["USERNAME"],
                                    password = app.config["DATABASEVK"]["PASSWORD"],
                                    host = app.config["DATABASEVK"]["HOSTNAME"],
                                    port = app.config["DATABASEVK"]["PORT"],
                                    database = app.config["DATABASEVK"]["DATABASENAME"] )
    
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

def showDB():
    con,cur=getDbConnectionVK()
    try:
        cur.execute("SELECT * from questionPapers")
        rows = cur.fetchall()
        all_data=[{"Course Code":row[0],"Course Title":row[1],"Year":row[2],"URL":row[3]} for row in rows]
        closeDbConnection(con, cur)
        return all_data
    except(Exception) as error:
        closeDbConnection(con, cur)
        return [ {"message": str(error)}  ]

class TeamTomato(Resource):
    def get(self):
        return "Team Tomato welcomes you"

# API - CRUD
class List(Resource):
    def get(self):
        vk=showDB()
        if len(vk)!=0:
            return jsonify(vk)
        return "No QuestionPaper Found"

class AddToList(Resource):
    def post(self):
        new_subject=request.get_json()
        con,cur=getDbConnectionVK()
        try:
            cc=new_subject["Course Code"]
            ct=new_subject["Course Title"]
            cy=new_subject["Year"]
            cu=new_subject["URL"]
            cur.execute(insertIntoTable,(cc,ct,cy,cu))
            con.commit()
        except(Exception) as error:
            closeDbConnection(con, cur)
            return [ {"message": str(error)}  ]
        closeDbConnection(con, cur)
        return jsonify(new_subject)

class UpdateCourseCode(Resource):
    def put(self,old,latest):
        con,cur=getDbConnectionVK()
        try:
            cur.execute(updateTable,(latest,old))
            con.commit()
            db=showDB()
            closeDbConnection(con, cur)
        except(Exception) as error:
            closeDbConnection(con, cur)
            return [ {"message": str(error)}  ]
        return jsonify(db)

class DeleteCourse(Resource):
    def delete(self,code):
        con,cur=getDbConnectionVK()
        try:
            cur.execute(deleteTable.format(code))
            con.commit()
            db=showDB()
            closeDbConnection(con, cur)
        except(Exception) as error:
            closeDbConnection(con, cur)
            return [ {"message": str(error)}  ]
        return jsonify(db)

#GET Method
api.add_resource(questionPaper, '/api/v1/teamtomato/')
api.add_resource(TeamTomato, '/')
api.add_resource(List,'/R')

#POST Method
api.add_resource(AddToList,'/C')                                        
                                             
#PUT Method
api.add_resource(UpdateCourseCode,'/U/<string:old>/<string:latest>')    

#DELETE Method
api.add_resource(DeleteCourse,'/D/<string:code>')                       


if __name__ == "__main__":
    # app.run()
    # serve(app, port=(process.env.PORT or 4950))
    con,cur=getDbConnectionVK()
    cur.execute("CREATE TABLE questionPapers(CODE TEXT,NAME TEXT,YEAR INT,URL TEXT);")
    con.commit()
    con.close()
    serve(app)
