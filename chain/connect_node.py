import requests
import json

d1 = {
    "nodes": ["http://127.0.0.1:5002",
              "http://127.0.0.1:5003"]
}

d2= {
    "nodes": ["http://127.0.0.1:5001",
              "http://127.0.0.1:5003"]
}

d3= {
    "nodes": ["http://127.0.0.1:5001",
              "http://127.0.0.1:5002",]
}

res1 = requests.post('http://192.168.29.188:5001/connect_node', json=d1)
res2 = requests.post('http://192.168.29.188:5002/connect_node', json=d2)
res3 = requests.post('http://192.168.29.188:5003/connect_node', json=d3)

print(res1.json())
print(res2.json())
print(res3.json())

inp= input("Press any key to exit:")
exit(1)