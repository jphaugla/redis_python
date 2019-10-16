def cache_request(conn, request, callback):
	if not can_cache(conn, request):
		return callback(request)
# If we can't cache the request, immediately call the callback.
# Convert the request into a simple string key for later lookups.
	page_key = 'cache:' + hash_request(request)
# Fetch the cached content if we can, and it's available.
	content = conn.get(page_key)
	if not content:
# Generate the content if we can't cache the page, or if it wasn't cached.
		content = callback(request)
# Cache the newly generated content if we can cache it.
		conn.setex(page_key, content, 300)
	return content
