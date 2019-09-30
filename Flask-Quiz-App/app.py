from flask import Flask,make_response,render_template, request, jsonify, json,jsonify
from flask import make_response, request, current_app, redirect, url_for, send_from_directory
import os,time,datetime
import  random
from flask_sqlalchemy import SQLAlchemy

#Init app
app = Flask(__name__)
#Database
app.config['SQLALCHEMY_DATABASE_URE'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
#Init db
db = SQLAlchemy(app)

#Questions class/Model
# class Questions(db.Model):
#     qno = db.Column(db.Integer, primary_key = True)
#     ques = db.Column(db.String(200), unique = True, nullable = False)
#     opt1 = db.Column(db.String(100), unique = True, nullable = True)
#     opt2 = db.Column(db.String(100), unique = True, nullable = True)
#     opt3 = db.Column(db.String(100), unique = True, nullable = True)
#     opt4 = db.Column(db.String(100), unique = True, nullable = True)
#     ans = db.Column(db.String(100), unique = True, nullable = False)
    
#     def __init__(self, ques, opt1, opt2, opt3, opt4, ans):
#         self.ques = ques
#         self.opt1 = opt1
#         self.opt2 = opt2
#         self.opt3 = opt3
#         self.opt4 = opt4
#         self.ans = ans



# #User class/Model
# class Users(db.Model):
#     user_id = db.Colum(db.Integer, primary_key = True)
#     user_name = db.Colum(db.String(100), primary_key = True)
    

# #Exam class/Model
# class Exam(db.Model):
#     id = db.Colum(db.Integer, primary_key = True)
#     user_id = db.Column(db.Integer, unique = True, nullable = False)
#     qno = db.Column(db.Integer, nullable = False)
#     ans = db.Column(db.String(2), nullable = False)    


# #Create a question
# @app.route('/question', methods = ['POST'])
# def create_ques():
#     ques = requests.json['question']
#     opt1 = requests.json['opt1']
#     opt2 = requests.json['opt2']
#     opt3 = requests.json['opt3']
#     opt4 = requests.json['opt4']
#     ans = requests.json['ans']

#     new_ques = Questions(ques, opt1, opt2, opt3, opt4, ans)
#     db.session.add(new_ques)
#     db.session.commit()

numberOfQuestions = 3
qns = {
    "section1": [
                ["q1","What is your name?",["Ram","Prem","Raghu","peter"],"Prem"],
                # ["q2","Where are you?",["bangalore","Pune","Chennai"],"bangalore"],
                # ["q3","What is your fav food?",["a","b","c","d"],"b"],
                # ["q4","q4?",["a","b","c","d"],"b"],
                # ["q5","q5?",["a","b","c","d"],"b"]
                ],
    "section2": [
                ["q21","What is your name?",["Ram","Prem","Raghu","peter"],"Prem"],
                # ["q22","Where are you?",["bangalore","Pune","Chennai"],"bangalore"],
                # ["q23","What is your fav food?",["a","b","c","d"],"b"],
                # ["q24","q4?",["a","b","c","d"],"b"],
                # ["q25","q5?",["a","b","c","d"],"b"]
                ],
    "section3": [
                ["q41","What is your name?",["Ram","Prem","Raghu","peter"],"Prem"],
                # ["q42","Where are you?",["bangalore","Pune","Chennai"],"bangalore"],
                # ["q43","What is your fav food?",["a","b","c","d"],"b"],
                # ["q44","q4?",["a","b","c","d"],"b"],
                # ["q45","q5?",["a","b","c","d"],"b"]
                ],                
    "section4": [
                ["q61","What is your name?",["Ram","Prem","Raghu","peter"],"Prem"],
                # ["q62","Where are you?",["bangalore","Pune","Chennai"],"bangalore"],
                # ["q63","What is your fav food?",["a","b","c","d"],"b"],
                # ["q64","q4?",["a","b","c","d"],"b"],
                # ["q65","q5?",["a","b","c","d"],"b"]
                ],
    "section5": [
                ["q81","What is your name?",["Ram","Prem","Raghu","peter"],"Prem"],
                # ["q82","Where are you?",["bangalore","Pune","Chennai"],"bangalore"],
                # ["q83","What is your fav food?",["a","b","c","d"],"b"],
                # ["q84","q4?",["a","b","c","d"],"b"],
                # ["q85","q5?",["a","b","c","d"],"b"]
                ]

}

@app.route('/getQuestions/',methods=['POST'])
def getQuestions():
    sectionId = request.form['sectionId']
    
    sections = ["section1","section2","section3"]

    questions =  qns[sectionId]#random.sample(qns[sectionId],numberOfQuestions)

    #Find the next section
    if sections.index(sectionId)==len(sections)-1:
        Next = "Finish"
    else:
        Next = sections[sections.index(sectionId)+1]
        print("next", Next)
    
    print("data", questions, Next, sectionId)
    return jsonify(qns=questions,next=Next)

@app.route('/')
@app.route('/index')
def index():
    #return make_response(send())
    #headers = {'Content-Type': 'text/html'}    
    return make_response(render_template('index2.html'),200)

if __name__ == '__main__':
      #ui.run() 
	  app.run(debug=True)
