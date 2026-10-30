from main import r

r.delete('queue:emails', 'queue:emails2')
 
r.lpush('queue:emails', 'a@x.com', 'b@x.com')     # LPUSH
r.rpush('queue:emails', 'c@x.com', 'd@x.com')     # RPUSH
r.lpushx('queue:emails', 'e@x.com')               # LPUSHX (only if exists)
r.rpushx('queue:emails', 'f@x.com')               # RPUSHX
 
print(r.lpop('queue:emails'))                     # LPOP
print(r.rpop('queue:emails', count=2))            # RPOP with count
 
print(r.lrange('queue:emails', 0, -1))            # LRANGE
print(r.lindex('queue:emails', 0))                # LINDEX
r.lset('queue:emails', 0, 'updated@x.com')        # LSET
 
r.linsert('queue:emails', 'BEFORE', 'updated@x.com', 'new@x.com')  # LINSERT
r.lrem('queue:emails', 1, 'new@x.com')            # LREM
print(r.llen('queue:emails'))                     # LLEN
r.ltrim('queue:emails', 0, 2)                     # LTRIM
 
r.rpoplpush('queue:emails', 'queue:emails2')      # RPOPLPUSH
r.lmove('queue:emails', 'queue:emails2', 'LEFT', 'RIGHT')  # LMOVE
 
job = r.blpop(['queue:emails'], timeout=1)        # BLPOP (blocking)
print(job)
r.brpop(['queue:emails'], timeout=1)            # BRPOP (blocking, mirror of BLPOP)