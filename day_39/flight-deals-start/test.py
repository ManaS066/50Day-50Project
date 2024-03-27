import requests
end = "https://api.sheety.co/b53bce2bcb7dead9ce55d6c92a902994/flightDeals/prices"

res =requests.get(end)
print(res.json())