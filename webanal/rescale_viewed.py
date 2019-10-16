def rescale_viewed(conn):
	while not QUIT:
# Remove any item not in the top 20,000 viewed items.
		conn.zremrangebyrank('viewed:', 20000, -1)

# Rescale all counts to be 1/2 of what they were before.
		conn.zinterstore('viewed:', {'viewed:': .5})

		time.sleep(300)

