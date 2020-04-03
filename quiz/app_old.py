from flask import Flask,make_response,render_template, request, jsonify, json,jsonify
from flask import make_response, request, current_app, redirect, url_for, send_from_directory
import os,time,datetime
import  random

app = Flask(__name__)

numberOfQuestions = 3
qns = {
    "section1": [
                ["q1","Athene founded in which year?",["2001","2010","2012","2013"],"2013"]
                ],
    "section2": [
                ["q2","Athene new policy admin system?",["OPAS","ALIP","AS400", "None of the above"],"ALIP"]
                ],
    "section3": [
                ["q3","Highest Stock Price of Athene ever reached?",[">$50",">$45 & <$50","$40> & <$45","None of the above"],"None of the above"]
                ],                
    "section4": [
                ["q4","Total No of product Athene sell ?",["4","5","6","7"],"6"]
                ],
    "section5": [
                ["q5","EDM Stands for?",["Enterprise Database Management","Enterprise Data Management","Enterprise Database Manage","None of the above"],"Enterprise Data Management"]
                ]

}

@app.route('/getQuestions/',methods=['POST'])
def getQuestions():
    sectionId = request.form['sectionId']
    
    sections = ["section1","section2","section3", "section4", "section5"]

    questions =  qns[sectionId]#random.sample(qns[sectionId],numberOfQuestions)

    #Find the next section
    if sections.index(sectionId)==len(sections)-1:
        Next = "Finish"
    else:
        Next = sections[sections.index(sectionId)+1]

    return jsonify(qns=questions,next=Next)

@app.route('/')
@app.route('/index')
def index():
    #return make_response(send())
    #headers = {'Content-Type': 'text/html'}    
    return make_response(render_template('index2.html'),200)

if __name__ == '__main__':
      app.run(debug=True)
