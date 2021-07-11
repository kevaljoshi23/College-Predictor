import requests

url = 'http://localhost:5000/predict_api_ms'
r = requests.post(url,json={'GRE Score':300,'TOEFL Score':118,'University Rating':4,'SOP':4.5,'LOR':4.5,'CGPA':9.65,'Research':1})

print(r.json())



