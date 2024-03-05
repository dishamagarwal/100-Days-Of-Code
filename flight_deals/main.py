from data_manager import DataManager
from flight_search import FlightSearch

def Main():
    destination_data = {}   # 'city' : details
    data_manager = DataManager()
    flight_search = FlightSearch()
    data_manager.format_destination_data(destination_data)

    # update_iata_codes in google sheets
    for item in destination_data:
        destination_data[item]['iataCode'] = flight_search.get_destination_code(item)
    data_manager.add_iata_code(destination_data)
        
if __name__ == '__main__':
    Main()
    