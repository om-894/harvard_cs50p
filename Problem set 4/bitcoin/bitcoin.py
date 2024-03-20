
# https://api.coindesk.com/v1/bpi/currentprice.json

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    try:
        float(sys.argv[1])  # expecting a number, hence the use of a ValueError
    except ValueError:
        sys.exit("Command-line argument is not a number")
    # print(request.json())
    # print(json.dumps(request.json(), indent = 2))
    data = request.json()
    bpi = data["bpi"] # ["USD"]["rate"] # dictionary, within dictionary, within dictionary!
    usd = bpi["USD"]
    price = usd["rate"]
    price = price.replace(",", "")
    price = float(price) * float(sys.argv[1])
    print(f"${price:,.4f}")
