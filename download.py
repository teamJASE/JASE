import os
import requests

URL_PREFIX = 'https://tb-hackathon-readonly.s3.us-west-2.amazonaws.com/'

FILES = ["xbt.usd.2018", "xbt.usd.2020", "eth.usd.2018", "eth.usd.2020"]

for name in FILES:
    url = URL_PREFIX + name
    response = requests.get(url)
    with open(name + '.csv', 'wb') as f:
        f.write(response.content)
