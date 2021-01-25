import json

f = open("nawa_telega.json", 'r', encoding="utf-8")
my_di = json.load(f)
f.close()

print(my_di)
