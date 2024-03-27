from pprint import pprint
import requests


class DataManager:
    def __init__(self):
        self.endpoint = "https://api.sheety.co/b53bce2bcb7dead9ce55d6c92a902994/flightDeals/prices"
        self.modify = "https://api.sheety.co/b53bce2bcb7dead9ce55d6c92a902994/flightDeals/prices/"

    def update_price(self, id, config):
        endpoint = f"{self.modify}/{id}"
        response = requests.put(endpoint, json=config)
        return response.json()

# Example usage:
if __name__ == "__main__":
    data_manager = DataManager()
    id = 7
    config = {
        "price": {
            "lowest price": 100
        }
    }
    resp = data_manager.update_price(id, config)

    pprint(resp)
    # res = requests.get(end)
    # pprint(res.json())
