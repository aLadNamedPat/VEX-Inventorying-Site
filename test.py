import json

# Opening JSON file
f = open('items.json')

# returns JSON object as
# a dictionary
data = json.load(f)

for i in data:
    print(i)

print(len(json.dumps(data)))
