from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__)

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Question

@app.route("/", methods=['GET'])
def get():
  return "<h1>Team Tomato welcome you</h1>"

@app.route("/api/v1/question/add", methods=['POST'])
def add_question():
    question_data = request.get_json()['question']

    subjectName = question_data['subjectName']
    shortForm = question_data['shortForm']
    staff = question_data['staff']
    year = question_data['year']
    url = question_data['url']

    try:
        question=Question(
            subjectName = subjectName,
            shortForm = shortForm,
            staff = staff,
            year = year,
            url = url
        )
        db.session.add(question)
        db.session.commit()
        res = {
          'id': question.id,
          'subjectName': question.subjectName,
          'shortForm': question.shortForm,
          'staff': question.staff,
          'year': question.year,
          'url': question.url
        }
        return jsonify(res)
    except Exception as e:
	    return(str(e))

@app.route("/api/v1/question/getall", methods=['GET'])
def get_all_questions():
    try:
        questions=Question.query.all()
        return  jsonify([e.serialize() for e in questions])
    except Exception as e:
	    return(str(e))

@app.route("/api/v1/question/<id_>", methods=['GET'])
def get_question_by_id(id_):
    try:
        question=Question.query.filter_by(id=id_).first()
        return jsonify(question.serialize())
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run()