import requests

parameter = {
    "amount": 10,
    "category": 15,
    "type": "boolean"

}
response = requests.get("https://opentdb.com/api.php", parameter)
response.raise_for_status()
question_data = response.json()["results"]

