import json
import requests

def main():
    url = "https://api.tequila.kiwi.com/v2/search"
    api_key = "I-eFlxQsXzJyT6x3xHf2sUDgGYVQ_-cu"
    headers = {"apikey": api_key}
    origin = {'BOS', 'NYC'}
    dest = {'BLR', 'BOM'}
    data = []
    for departure in origin:
        for destination in dest:
            query = {
                'fly_from': departure,
                'fly_to': destination,
                'date_from': '15/05/2024',
                'date_to': '15/06/2024',
                'return_from': '01/07/2024', 
                'return_to': '01/08/2024',  
                'nights_in_dst_from': 35,
                'nights_in_dst_to': 45,
                'price_to': 955,
                'stopover_from': '2:00',
                'max_stopovers': 2
            }
            response = requests.get(url=url, headers=headers, params=query)
            if  response.status_code != 200:
                print('error')
                print(response.json())
                break
            data += response.json()['data']  # Extracting 'data' directly from the JSON response

    for flight in data:
        # if flight['price'] * 2 < 1000:
        origin_city = flight['cityFrom']
        destination_city = flight['cityTo']
        price = flight['price']
        departure_date_outbound = flight['route'][0]['local_departure'][:10]  # Departure date for the outbound leg
        departure_date_return = flight['route'][1]['local_departure'][:10]  # Departure date for the return leg
        flight_no_departure = flight['route'][0]['flight_no']
        flight_no_return = flight['route'][1]['flight_no']
        
        print(f"Origin City: {origin_city}, Destination City: {destination_city}, Price: ${price}")
        print(f"Outbound Departure Date: {departure_date_outbound}, Return Departure Date: {departure_date_return}")
        print(f"Departure Flight No: {flight_no_departure}, Return Flight No: {flight_no_return}")

if __name__ == '__main__':
    main()