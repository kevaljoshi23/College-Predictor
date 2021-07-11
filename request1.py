import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'10th Marks':86,'12th Marks':89,'AIEEE Rank':4563})


print(r.json())


