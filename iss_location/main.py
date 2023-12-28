import requests

class Main():
    respone = requests.get(url="http://api.open-notify.org/iss-now.json")
    respone.raise_for_status()

    data = respone.json()
    print(data["iss_position"])