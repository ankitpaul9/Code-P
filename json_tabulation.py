from datetime import datetime
from tabulate import tabulate
import json

data = json.loads(open('/home/paulin/Documents/data.json').read())
table=[]
headers = ['ID','Name','Message','Link','Date']

for p in data['maps']:
    idd=p['id']
    name=p['name']
    msg=p['message']
    link=p['actions'][0]['link']
    date=datetime.strptime(p['created_time'], '%Y-%m-%dT%H:%M:%S+0000').strftime("%m/%d/%y")
    table.append([idd,name,msg,link,date])


print tabulate(table, headers, tablefmt="fancy_grid")
