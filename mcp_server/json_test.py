import json
rates = ["NYC", "BLN", "CHI"]
data = json.loads('{"one": "1", "two": "2", "three": "3"}')
for i in range(len(rates)):
    print(rates[i])