from coinbase.rest import RESTClient
from json import dumps
from keys import api_key, api_secret


client = RESTClient(api_key=api_key, api_secret=api_secret)

accounts = client.get_accounts()
print(dumps(accounts, indent=2))