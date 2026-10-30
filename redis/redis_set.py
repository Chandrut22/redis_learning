from main import r

r.delete('post:1:tags', 'post:2:tags', 'tags:union', 'tags:diff', 'tags:moved')
 
r.sadd('post:1:tags', 'python', 'redis')          # S ADD
r.sadd('post:2:tags', 'redis', 'nosql')
r.srem('post:2:tags', 'nosql')                    # S REMOVE
r.sadd('post:2:tags', 'nosql')                    # re-add for demo
 
print(r.smembers('post:1:tags'))                  # S MEMBERS
print(r.sismember('post:1:tags', 'redis'))        # S ISMEMBER
print(r.smismember('post:1:tags', ['redis', 'java']))  # S MISMEMBER
print(r.scard('post:1:tags'))                     # S CARD (Unique)
 
print(r.spop('post:1:tags', count=1))             # S POP
r.sadd('post:1:tags', 'python')                   # restore for demo
print(r.srandmember('post:1:tags', number=1))     # S RAND MEMBER
 