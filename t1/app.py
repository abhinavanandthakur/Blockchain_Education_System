from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/student_details', methods =["GET", "POST"])
def initiate_student_details():
    if request.method == "POST":
       
       to = request.form.get("to")
       content_type = request.form.get("content_type")
       content_topic = request.form.get("content_topic")
       content_code = request.form.get("content_code")
       score= request.form.get("score")
       feedback= request.form.get("feedback")
       Student_details(to, content_type, content_topic, content_code, score, feedback)
    return render_template("home.html")   
    
if __name__ == '__main__':
   app.run()


# flask run -h localhost -p 5004