import json
import sys
import requests


try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    r = r.json()

except requests.RequestException:
    pass


try:
    amount = float(sys.argv[1]) * r["bpi"]["USD"]["rate_float"]

    print(f"${amount:,.4f}")
except IndexError:
    print("Missing command-line argument")
    sys.exit(1)
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)




