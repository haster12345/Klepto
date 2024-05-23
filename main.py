from coinbase.rest import RESTClient
from json import dumps
from keys import api_key, api_secret
import math

client = RESTClient(api_key=api_key, api_secret=api_secret)

accounts = client.get_accounts()
# print(dumps(accounts, indent=2))


product = client.get_product("BTC-USD")
print(product)

btc_usd_price = float(product["price"])
adjusted_btc_usd_price = str((math.btc_usd_price - (btc_usd_price * 0.05)))

print(adjusted_btc_usd_price)

order = client.market_order_buy(
    client_order_id="00000001",
    product_id="BTC-GBP",
        quote_size="0.01"
    )

order_id = order["order_id"]

fills = client.get_fills(order_id=order_id)
print(dumps(fills, indent=2))
