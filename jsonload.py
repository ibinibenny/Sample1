import json
f=open("json.txt","r")
print(json.loads(f.read()))
f.close()
