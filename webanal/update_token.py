def update_token(conn, token, user, item=None):
	timestamp = time.time()
	conn.hset('login:', token, user)
	conn.zadd('recent:', token, timestamp)
	if item:
		conn.zadd('viewed:' + token, item, timestamp)
		conn.zremrangebyrank('viewed:' + token, 0, -26)
		conn.zincrby('viewed:', item, -1)
