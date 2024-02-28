## Parsing Json
import json
x='{"name":"Mohan","age":30,"city":"New York"}'
y=json.loads(x)
print(y)


type(y)

y['age']

##Converting to JSON

x={
'name':'Harshal'
'age': 20,
'City':'New York'
}
y=json.dumps(x)
print(y)
type(y)
type(x)

