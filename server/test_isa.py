import requests

url = "http://127.0.0.1:5000/add"
data = {"name": "Alice", "age": 30}

response = requests.post(url, json=data)
print(response.json())
print("Test script is running successfully!")
