import json

with open('/Users/yogesh.kalbhore/Documents/Office/Automation/python/.vscode/testdata.json') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
