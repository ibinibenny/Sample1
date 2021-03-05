import json
f=open("json.txt","r")
x=f.read()
y=json.dumps(x)
print(type(y))
f.dump(y,f)
f.close()
