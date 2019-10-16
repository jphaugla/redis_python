def schedule_row_cache(conn, row_id, delay):
	conn.zadd('delay:', row_id, delay)
# Set the delay for the item first.
	conn.zadd('schedule:', row_id, time.time())
