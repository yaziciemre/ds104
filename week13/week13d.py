
import redis
import json


r = redis.Redis(host='localhost', port=6379, db=0)

mydata = {'a': 3, 'b': 4}


r.set('a', mydata!!!) # 4 ==> '4'
value = r.get('a').decode('utf-8') # READ
print("REDIS", value)

user = {
	'friends': ['ahmet', 'mehmet', 'mustafa', 'anar', 'gultaj'],
	'posts': ['i went to istanbul ....', 'asdfsafda'],
	'': []
}