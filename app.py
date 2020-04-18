import os
import json
import flask
import requests
import psycopg2
from flask import request,jsonify
from waitress import serve
from databaseScripts.searchQueries import *
from flask_restful import reqparse, Api, Resource
from flask_sqlalchemy import SQLAlchemy

# Initialize the App
app = flask.Flask(__name__)
#Dev environment    - config/config.json
#Prod environement  - config/productionConfig.json
app.config.from_json(os.path.join(os.path.abspath(os.getcwd()),'config/config.json'))
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db=SQLAlchemy(app)


# Parsable arguments
parser = reqparse.RequestParser()
parser.add_argument('keyword')

# Python object for questionPapers table
class Subject(db.Model):
    __tablename__ = 'questionpapers'
    name=db.Column('name',db.String(25), primary_key = True)
    code=db.Column('code',db.String(25))
    year=db.Column('year',db.Integer)
    url=db.Column('url',db.String(25))


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

def showDB():
    try:
        rows=Subject.query.all()
        all_data=[{"Course Code":row.code,"Course Title":row.name,"Year":row.year,"URL":row.url} for row in rows]
    except(Exception) as error:
        return {"message": str(error)}
    return all_data

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
        try:
            sub=Subject(name=new_subject["Course Title"],code=new_subject["Course Code"],year=new_subject["Year"],url=new_subject["URL"])
            db.session.add(sub)
            db.session.commit()
        except(Exception) as error:
            return {"message": str(error)}
        return "success"

class UpdateCourseCode(Resource):
    def put(self,old,latest):
        try:
            you=Subject.query.filter_by(code=old).update({Subject.code:latest})
            db.session.commit()
        except(Exception) as error:
            return {"message": str(error)}
        return "success"

class DeleteCourse(Resource):
    def delete(self,code):
        try:
            sub=Subject.query.filter_by(code=code).all()
            for i in sub:
                db.session.delete(i)
            db.session.commit()
        except(Exception) as error:
            return {"message": str(error)}
        return "success"

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
    serve(app)