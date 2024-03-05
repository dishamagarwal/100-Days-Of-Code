import requests

class DataManager:
    username = "dishaagarwal"
    password = "Disha1123$"
    base_url = "https://api.sheety.co/258a068324ce73e52063cb14540c5c78/flightDeals/sheet1"
    
    def format_destination_data(self, destination_data):
        response = requests.get(self.base_url, auth=(self.username, self.password))
        data = response.json()["sheet1"]
        for item in data:
            destination_data[item['city']] = {
                    'iataCode': item['iataCode'], 
                    'lowestPrice': item['lowestPrice'], 
                    'id': item['id']
                }
    
    def add_iata_code(self, destination_data):
        for item in destination_data:
            # structuring body format for cell to be edited
            new_data = {
                "sheet1" : {
                        "iataCode": destination_data[item]["iataCode"]
                }
            }
            # adding the iata codes to excel
            response = requests.put(
                url=f"{self.base_url}/{destination_data[item]['id']}",
                auth=(self.username, self.password),
                json=new_data
            )