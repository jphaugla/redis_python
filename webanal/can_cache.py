def can_cache(conn, request):
# Get the item ID for the page, if any.
	item_id = extract_item_id(request)

# Check whether the page can be statically cached and whether this is an item page.
	if not item_id or is_dynamic(request):

		return False
# Get the rank of the item.
	rank = conn.zrank('viewed:', item_id)

	return rank is not None and rank < 10000
