from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#Questions class/Model
class Questions(db.Model):
    __tablename__ = 'questions'
    qno = db.Column(db.Integer, primary_key = True)
    ques = db.Column(db.String(200), unique = True, nullable = False)
    option1 = db.Column(db.String(100), unique = True, nullable = True)
    option2 = db.Column(db.String(100), unique = True, nullable = True)
    option3 = db.Column(db.String(100), unique = True, nullable = True)
    option4 = db.Column(db.String(100), unique = True, nullable = True)
    answer = db.Column(db.String(100), unique = True, nullable = False)
    
    def __init__(self, ques, option1, option2, option3, option4, answer):
        self.ques = ques
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.answer = answer

    def serialize(self):
        return {
             'question' : self.ques,
             'opt1': self.option1,
             'opt2': self.option2,
             'opt3': self.option3,
             'opt4': self.option4,
             'ans': self.answer
        }