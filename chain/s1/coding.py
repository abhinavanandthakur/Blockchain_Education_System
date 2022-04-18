import requests
import json
import webbrowser
import hashlib

coding_topic= input("Enter Coding_topic:")
code_file= input("Enter File name of the code:")
language=input("Enter the programming language:")

h = hashlib.sha1()
with open(code_file,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   
hash_value= h.hexdigest()

dictToSend =     {"From": "Abhinav",
                  "To": "Vivek",
                  "Amount": "0",
                  "Content_Type": f"Coding({language})",
                  "Content_Topic": coding_topic,
                  "Content_Code": hash_value,
                  "Assesment_Score": "",
                  "Feedback":""
                  }

res = requests.post('http://192.168.29.188:5001/add_transaction', json=dictToSend)

print("The code hash has been successfully captured in the chain.\nSubmit the code to the instructor with the hash value.\nSave your code safely for future references.")
