def cache_rows(conn):
	while not QUIT:
# Find the next row that should be cached (if any), including the timestamp, as a list of tuples with zero or one items.
		next = conn.zrange('schedule:', 0, 0, withscores=True)

		now = time.time()
		if not next or next[0][1] > now:
# No rows can be cached now, so wait 50 milliseconds and try again.
			time.sleep(.05)

			continue

		row_id = next[0][0]
		delay = conn.zscore('delay:', row_id)
# Get the delay before the next schedule.

		if delay <= 0:
			conn.zrem('delay:', row_id)
			conn.zrem('schedule:', row_id)
			conn.delete('inv:' + row_id)
# The item shouldn't be cached anymore; remove it from the cache.

			continue

		row = Inventory.get(row_id)
# Get the database row.

		conn.zadd('schedule:', row_id, now + delay)
		conn.set('inv:' + row_id, json.dumps(row.to_dict()))
# Update the schedule and set the 
