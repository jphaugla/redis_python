import time
def update_token(conn, token, user, item=None):
# Get the timestamp.
	timestamp = time.time()
	print("the timestamp is " + str(timestamp))

# Keep a mapping from the token to the logged-in user.
	conn.hset('login:', token, user)
# Record when the token was last seen.
	conn.zadd('recent:', {token : timestamp})
	if item:
# Record that the user viewed the item.
		conn.zadd('viewed:' + token, {item:timestamp})
# Remove old items, keeping the most recent 25.
		conn.zremrangebyrank('viewed:' + token, 0, -26)
def check_token(conn, token):
	return conn.hget('login:', token)
