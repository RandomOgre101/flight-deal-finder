import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/e44555c176f80a2a513f65568432fdf1/flightDeals/prices"


class DataManager:
    def __init__ (self):
        self.data = {}

    def get_sheety(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        self.data = response.json()
        return self.data


    def put_iata(self):
        for city in self.data['prices']:
            updated = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=updated)

    def get_emails(self):
        customers_endpoint = SHEETY_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data