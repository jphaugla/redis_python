QUIT = False
LIMIT = 10000000
def clean_sessions(conn):
	while not QUIT:
# Find out how many tokens are known.
		size = conn.zcard('recent:')
		if size <= LIMIT:
# We're still under our limit; sleep and try again.
			time.sleep(1)
		continue
	end_index = min(size - LIMIT, 100)
# Fetch the token IDs that should be removed.
	tokens = conn.zrange('recent:', 0, end_index-1)
	session_keys = []
	for token in tokens:
# Prepare the key names for the tokens to delete.
		session_keys.append('viewed:' + token)
	conn.delete(*session_keys)
	conn.hdel('login:', *tokens)
	conn.zrem('recent:', *tokens)
