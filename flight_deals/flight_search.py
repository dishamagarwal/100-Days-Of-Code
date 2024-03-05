import requests

class FlightSearch:
    api_key = "I-eFlxQsXzJyT6x3xHf2sUDgGYVQ_-cu"
    url = "https://api.tequila.kiwi.com"

    def get_destination_code(self, city_name):
        location_endpoint = f"{self.url}/locations/query"
        headers = {"apikey": self.api_key}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        return response.json()['locations'][0]['code']
    
    def get_flight_prices(self, destination_data):
        search_endpoint = f"{self.url}/search"
        headers = {"apikey": self.api_key}
        # run the call for all cities for the next 6 months
        for item in destination_data:
            query = {
                "fly_from": 'NYC',
                "fly_to": destination_data[item]['iataCode'],
                "date_from": '01/04/2021', #example
                "date_to": "",
                "return_from": "",
                "return_to": "",
                "one_for_city": 1,
                "selected_cabins": 'W',
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "price_to": "dvidjfv"
                }