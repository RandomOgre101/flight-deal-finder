from data_manager import DataManager
from pprint import pprint


data_manager = DataManager()
sheet_data = data_manager.get_sheety()


if sheet_data['prices'][0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data['prices']:
        row['iataCode'] = flight_search.get_code(row['city'])


data_manager.put_iata()

