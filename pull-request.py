import requests
import json

url = "https://api.apilayer.com/exchangerates_data/latest?symbols=USD,BRL,EUR,BTC,ETH&base=USD"

payload = {}
headers = {"apikey": "Wp6Wdicd1vKZqo0wyK6JZ00wtaPSjPBT"}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text

print(result)

