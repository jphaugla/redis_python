import redis
conn = redis.Redis()
conn.set('foo','bar')
conn.set('jason','supercool')
