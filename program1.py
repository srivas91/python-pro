import json
d={'id':101}
s=json.dumps(d)
print(s)

n=json.loads(s)
print(n)