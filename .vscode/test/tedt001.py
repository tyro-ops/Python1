import requests
import pprint
import csv
import json
from pathlib import Path
home = str(Path.home())
smd = home+'/Documents/Office/Automation/python1/.vscode/test/csv.csv'
print(smd)


url = 'https://randomuser.me/api/?results=1'
headers = {'authorization': "Basic API Key Ommitted",
           'accept': "application/json", 'accept': "text/csv"}

users = requests.get(url, headers=headers).json()
pprint.pprint(users)
result = json.dumps(users)

f = open(home+'/Documents/Office/Automation/python1/.vscode/test/csv.csv', "w")
f.truncate(0)
f.write(result)
f.close()

f = open(home+'/Documents/Office/Automation/python1/.vscode/test/csv.xls', "w")
f.truncate(0)
f.write(result)
f.close()


with open(home+'/Documents/Office/Automation/python1/.vscode/test/test.json', 'w') as outfile:
    json.dump(result, outfile)
