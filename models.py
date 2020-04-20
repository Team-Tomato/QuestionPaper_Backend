from app import db

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    subjectName = db.Column(db.String())
    shortForm = db.Column(db.String())
    staff = db.Column(db.String())
    year = db.Column(db.Integer)
    url = db.Column(db.String())

    def __init__(self, subjectName, shortForm, staff, year, url):
        self.subjectName = subjectName
        self.shortForm = shortForm
        self.staff = staff
        self.year = year
        self.url = url

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'subjectName': self.subjectName,
            'shortForm': self.shortForm,
            'staff':self.staff,
            'year' :self.year,
            'url' :self.url
        }