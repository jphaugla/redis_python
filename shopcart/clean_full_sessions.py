def clean_full_sessions(conn):
	while not QUIT:
#   zcard returns the number of elements in the sorted list
		size = conn.zcard('recent:')
		if size <= LIMIT:
			time.sleep(1)
			continue

		end_index = min(size - LIMIT, 100)
		sessions = conn.zrange('recent:', 0, end_index-1)

		session_keys = []
		for sess in sessions:
			session_keys.append('viewed:' + sess)
# The required added line to delete the shopping cart for old sessions.
			session_keys.append('cart:' + sess)

		conn.delete(*session_keys)
		conn.hdel('login:', *sessions)
		conn.zrem('recent:', *sessions)
