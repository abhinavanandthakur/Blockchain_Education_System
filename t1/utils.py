import requests
import json

def Student_details(to, content_type, content_topic, content_code, score, feedback):
   
        dictToSend = {"From": "Vivek",
                  "To": to,
                  "Amount": 0,
                  "Content_Type": content_type,
                  "Content_Topic": content_topic,
                  "Content_Code": content_code,
                  "Assesment_Score": score,
                  "Feedback":feedback
                  }
        if(to.lower()=="abhinav" or to.lower()=="james"):
            res = requests.post('http://192.168.29.188:5003/add_transaction', json=dictToSend)
            print(res.json())
            
        else:
            print("Student Doesn't Exist")