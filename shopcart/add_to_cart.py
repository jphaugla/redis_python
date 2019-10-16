def add_to_cart(conn, session, item, count):
	if count <= 0:
# Remove the item from the cart.
		conn.hrem('cart:' + session, item)
	else:
# Add the item to the cart.
		conn.hset('cart:' + session, item, count)
