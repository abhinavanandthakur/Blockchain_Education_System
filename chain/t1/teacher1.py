import requests
import json

while True:
    response= int(input("Enter 1 to fill a student score/feedback/status, Enter 2 to exit:"))

    if(response==2):
        exit(1)

    elif (response!=2 and response!=1):
        pass

    else:
        to= input("Student Name/ Student ID:")
        content_type=input("Type of the content:")
        content_topic= input("Content Name/Topic:")
        content_code= input("Content Code/hash:")
        score= int(input("Score out of 100:"))
        feedback= input("Enter Feedback:")
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