import requests
from dateutil import parser
from datetime import datetime, timedelta

class Search:
    url = "https://api.tequila.kiwi.com/v2/search"
    # TODO: encrypt
    api_key = "I-eFlxQsXzJyT6x3xHf2sUDgGYVQ_-cu"
    # TODO: load from csv
    origin = {'BOS', 'NYC', 'SJC', 'SFO'}
    dest = {'BLR', 'BOM'}
    data = []
    flights = {}

    def search_flights(self):
        headers = {"apikey": self.api_key}
        for departure in self.origin:
            for destination in self.dest:
                query = {
                    'fly_from': departure,
                    'fly_to': destination,
                    'date_from': '15/05/2024',
                    'date_to': '01/07/2024',
                    'return_from': '01/07/2024', 
                    'return_to': '01/10/2024',  
                    'nights_in_dst_from': 35,
                    'nights_in_dst_to': 45,
                    'price_to': 1000,
                    'stopover_from': '2:00',
                    'max_stopovers': 2,
                    'adult_hold_bag': 1
                }
                response = requests.get(url=self.url, headers=headers, params=query)
                if  response.status_code != 200:
                    print('error')
                    print(response.json())
                    break
                self.data += response.json()['data']  # Extracting 'data' directly from the JSON response
        self.arrange_flight_info()

    def arrange_flight_info(self):
        for flight in self.data:
            departure_date_to_destination = flight['route'][0]['local_departure'][:10]

            itinerary = []
            for leg in flight['route']:
                itinerary.append({leg['flyFrom'], leg['flyTo']})
                # Extracting departure date for the first leg from destination
                if leg['return'] == 1:
                    departure_date_from_destination = leg['local_departure'][:10]

            print(flight['cityFrom'] + ' (' + str(round(flight['duration']['departure'] / 3600, 1)) + ' hrs)', ' -> ', 
                  flight['cityTo'] + ' (' + str(round(flight['duration']['return'] / 3600, 1)) + ' hrs)')
            print(departure_date_to_destination, ' -> ', departure_date_from_destination)
            print("Airline:", flight['airlines'][0])  # Assuming there's only one airline
            print("Itinerary:", itinerary)
            print("Total Cost:", flight['price'])
            print("\n")

            # store in db
            self.flights[id] = {
                'Origin': flight['cityFrom'],
                'Destination': flight['cityTo'],
                'Going Time': round(flight['duration']['departure'] / 3600, 1),
                'Return Time': round(flight['duration']['return'] / 3600, 1),
                "Airline": flight['airlines'][0],
                "Itinerary": itinerary,
                "Total Cost": flight['price']
            }