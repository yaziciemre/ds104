
print('program started')
#mydict = {'a': 3}
#a = 3  # WRITE
#print(mydict['a'])
#print(a) # READ

import redis

# Connect to the local Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Set a key-value pair in Redis, WRITE
#! r.set('a', '3')

# Get the value associated with the key 'foo'
value = r.get('a').decode('utf-8') # READ
print("REDIS", value)  # Output will be: b'bar'




# LAST LINE ==> close 
print('program ended')

# The variables a, mydict ==> are deleted from memory, because the program is closed!
