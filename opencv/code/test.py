import requests
while True:
    r = requests.get('http://localhost:8081')
    print(r.text)