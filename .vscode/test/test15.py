import requests
import pprint
import pytest

requests.__version__

url = 'https://randomuser.me/api/?results=1'
users = requests.get(url).json()
pprint.pprint(users)
