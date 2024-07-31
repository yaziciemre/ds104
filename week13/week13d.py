
import redis
import json


r = redis.Redis(host='localhost', port=6379, db=0)

mydata = {'a': 3, 'b': 4}

mystr =  '{"a": 3, "b": 4}'

s = ""
for x in mydata:
	s += x + "=" + mydata[x] + "\n"

s = """
a=3
b=4
"""


r.set('a', json.dumps(mydata)) # 4 ==> '4'
value = r.get('a').decode('utf-8') # READ
value = json.loads( value )
print("REDIS", value)

user = {
	'friends': ['ahmet', 'mehmet', 'mustafa', 'anar', 'gultaj'],
	'posts': ['i went to istanbul ....', 'asdfsafda'],
	'': []
}