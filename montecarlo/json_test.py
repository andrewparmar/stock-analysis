import requests

response = requests.get("https://query2.finance.yahoo.com/v7/finance/options/amd")
data = response.json()

call_options = data["optionChain"]["result"][0]["options"][0]["calls"]

for option in call_options:
	# print(option["strike"])
	print("{} {}".format(option["contractSymbol"], option["expiration"]))	
