from flask import Flask, render_template, request
from utils import *
from read import *
from code import *
app = Flask(__name__)

@app.route('/')
def home():
    videoLink = "https://www.youtube.com/watch?v=0EgpeYB115s"
    pdflink="https://drive.google.com/file/d/1em0rxeMkaLRwtAqDNPz_r6KTB9GnVKR_/view?usp=sharing"
    return render_template('home.html', data=videoLink, data2=pdflink)

@app.route('/form', methods= ['GET'])
def index_func():
    return render_template('coding.html')


@app.route('/video_quiz',methods=['POST'])
def initiate_quiz():
    handler()
    return render_template('home.html', response='{}'.format("Success"))

@app.route('/reading_quiz',methods=['POST'])
def initiate_reading_quiz():
    reading_quiz()
    return render_template('home.html', response='{}'.format("Success"))

@app.route('/coding_activity', methods =["GET", "POST"])
def initiate_coding_activity():
    if request.method == "POST":
       
       topic = request.form.get("topic")
       # getting input with name = lname in HTML form 
       file_name = request.form.get("file") 
       
       language= request.form.get("lang")
       code(topic,file_name,language)
       
    return render_template("coding.html")
    
if __name__ == '__main__':
   app.run()


# flask run -h localhost -p 5005