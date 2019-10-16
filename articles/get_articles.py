ARTICLES_PER_PAGE = 25
def get_articles(conn, page, order='score:'):
# Set up the start and end indexes for fetching the articles.
	start = (page-1) * ARTICLES_PER_PAGE
	end = start + ARTICLES_PER_PAGE - 1
# Fetch the article ids.
	ids = conn.zrevrange(order, start, end)
	articles = []
	for id in ids:
# Get the article information from the list of article ids.
		article_data = conn.hgetall(id)
		article_data['id'] = id
		articles.append(article_data)
	return articles
def get_group_articles(conn, group, page, order='score:'):
# Create a key for each group and each sort order.
	key = order + group
# If we haven't sorted these articles recently, we should sort them.
	if not conn.exists(key):
# Actually sort the articles in the group based on score or recency.
		conn.zinterstore(key,
			['group:' + group, order],
			aggregate='max',
		)
# Tell Redis to automatically expire the ZSET in 60 seconds.
		conn.expire(key, 60)
# Call our earlier get_articles() function to handle pagination and article data fetching.
	return get_articles(conn, page, key)

