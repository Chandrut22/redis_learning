from main import r

r.delete('leaderboard')
 
r.zadd('leaderboard', {'alice': 100, 'bob': 80, 'cara': 95})  # Z ADD
r.zrem('leaderboard', 'cara')                                  # Z REM
r.zadd('leaderboard', {'cara': 95})                            # re-add for demo
 
print(r.zscore('leaderboard', 'alice'))                        # Z SCORE
print(r.zmscore('leaderboard', ['alice', 'bob']))              # Z MSCORE
print(r.zincrby('leaderboard', 10, 'bob'))                     # Z INCR BY
 
print(r.zrange('leaderboard', 0, -1, withscores=True))         # Z RANGE
print(r.zrevrange('leaderboard', 0, -1, withscores=True))      # Z REV RANGE
print(r.zrangebyscore('leaderboard', 80, 100))                 # Z RANGE BY SCORE
print(r.zrevrangebyscore('leaderboard', 100, 80))              # Z REV RANGE BY SCORE
 
print(r.zrank('leaderboard', 'bob'))                           # Z RANK
print(r.zrevrank('leaderboard', 'bob'))                        # Z REV RANK
print(r.zcard('leaderboard'))                                  # Z CARD
print(r.zcount('leaderboard', 80, 100))                        # ZCOUNT
 
print(r.zpopmin('leaderboard', count=1))                       # ZPOPMIN
print(r.zpopmax('leaderboard', count=1))                       # ZPOPMAX
 

r.zadd('scores:a', {'x': 1, 'y': 2})
r.zadd('scores:b', {'x': 3, 'z': 4})
r.zunionstore('scores:union', ['scores:a', 'scores:b'])        # ZUNIONSTORE
r.zinterstore('scores:inter', ['scores:a', 'scores:b'])        # ZINTERSTORE
 
cursor, members = r.zscan('leaderboard', cursor=0)             # ZSCAN
print(members)
print(cursor)
print(r.zrange('leaderboard', 0, -1, withscores=True))  