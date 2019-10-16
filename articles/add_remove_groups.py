def add_remove_groups(conn, article_id, to_add=[], to_remove=[]):
# Construct the article information like we did in post_article.
	article = 'article:' + article_id
	for group in to_add:
# Add the article to groups that it should be a part of.
		conn.sadd('group:' + group, article)
	for group in to_remove:
# Remove the article from groups that it should be removed from.
		conn.srem('group:' + group, article)

