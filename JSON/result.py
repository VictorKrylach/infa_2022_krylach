import json

with open('values.json') as file:
    v = json.load(file)

with open('tests.json') as file:
    t = json.load(file)

val = v['values']

tes = t['tests']

for i in range(0, len(tes)):

	tes[i]['value'] = val[i]['value']

print (tes)

input () 
