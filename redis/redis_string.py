from main import r
import time

# r.set(
#     name,       # key
#     value,      # value
#     ex=None,    # expiration time in seconds
#     px=None,    # expiration time in milliseconds
#     nx=False,   # set only if key does NOT exist
#     xx=False    # set only if key already exists
# )

r.set('user:1:name', 'Asha')
r.set('user:1:name', 'Asha B', xx=True)     # only overwrite if key exists
r.set('otp:1029', '4471', ex=10, nx=True)   # one-time code, 10 TTL

# time.sleep(11)
# print(r.get('otp:1029'))

print(r.get('user:1:name'))                  # GET
print(r.getset('user:1:name', 'Asha C'))     # GETSET -> old value
print(r.get('user:1:name'))
print(r.getdel('otp:1029'))                  # GETDEL -> value, then deletes key

r.set('session:1', 'active')
print(r.getex('session:1', ex=60))           # GETEX -> value, refresh TTL

r.mset({'city:1': 'Chennai', 'city:2': 'Pune'})               # MSET
print(r.msetnx({'city:3': 'Mumbai'}))                         # MSETNX
print(r.mget(['city:1', 'city:2', 'city:3']))                 # MGET


r.append('log:1', 'first entry;')            # APPEND
r.append('log:1', 'second entry;')
print(r.get('log:1'))
print(r.strlen('log:1'))                      # STRLEN
print(r.getrange('log:1', 0, 10))             # GETRANGE
r.setrange('log:1', 0, 'FIRST')               # SETRANGE

r.set('views', 0)
print(r.incr('views'))                        # INCR
print(r.decr('views'))                        # DECR
print(r.incrby('views', 10))  
print(r.decrby('views', 3))                   # DECRBY
print(r.incrbyfloat('price', 2.5))            # INCRBYFLOAT
