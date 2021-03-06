from flask import Flask,make_response,render_template, request, jsonify, json,jsonify
from flask import make_response, request, current_app, redirect, url_for, send_from_directory
import os,time,datetime
import  random
from flask_sqlalchemy import SQLAlchemy
from models import db, Questions

#Init app
app = Flask(__name__)

#Init db
db = SQLAlchemy(app)

POSTGRES = {
    'user': 'postgres',
    #'pw': 'root',
    'pw': 'Rohit123',
    'db': 'examdb',
    #'host': 'localhost',
    'host': 'database-2.cfog6a1gwdlx.us-east-2.rds.amazonaws.com',
    'port': '5432',
}


#app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)


numberOfQuestions = 4
qns = {}

@app.route('/getQuestions/',methods=['POST'])
def getQuestions():
    sectionId = request.form['sectionId']
    
    sections = ["section1","section2","section3", "section4"]

    questions =  qns[sectionId]#random.sample(qns[sectionId],numberOfQuestions)

    #Find the next section
    if sections.index(sectionId)==len(sections)-1:
        Next = "Finish"
    else:
        Next = sections[sections.index(sectionId)+1]
        print("next", Next)
    
    print("data", questions, Next, sectionId)
    return jsonify(qns=questions,next=Next)


@app.route('/add_ques', methods = ['GET', 'POST'])
def add_ques():
    if request.method == 'POST':
        #Fetch form data
        ques_detail = request.form
        ques = ques_detail['question']
        opt1 = ques_detail['option1']
        opt2 = ques_detail['option2']
        opt3 = ques_detail['option3']
        opt4 = ques_detail['option4']
        ans = ques_detail['answer']

        ques_obj = Questions(ques, opt1, opt2, opt3, opt4, ans)
        db.session.add(ques_obj)
        db.session.commit()
    return render_template('feed_question.html')

def get_ques():
    i = 1
    all_ques = Questions.query.all()
    ques_set = random.sample(all_ques, numberOfQuestions)
    for row in ques_set:
        qns['section{}'.format(i)] = [['q{}'.format(i), row.ques, [row.option1, row.option2, row.option3, row.option4], row.answer]]
        i += 1


@app.route('/')
@app.route('/index')
def index():
    get_ques()
    #return make_response(send())
    #headers = {'Content-Type': 'text/html'}    
    return make_response(render_template('index2.html'),200)

if __name__ == '__main__':
      #ui.run() 
	  app.run(host = '127.0.0.1', debug=False)