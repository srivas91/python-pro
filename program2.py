import json
mystr='welcome to learn github'
with open('myfile.txt','w') as f:
    json.dump(mystr,f)

with open('myfile.txt','r') as f:
    mydata=json.load(f)
print(mydata)