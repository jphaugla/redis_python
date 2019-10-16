import time
# Prepare our constants.
ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432
# conn is a zset with article and the score is the time the article was posted
# article is a zset with article and the score being the article score
# user is the user
def article_vote(conn, user, article):
	print("entering article_vote") 
	cutoff = time.time() - ONE_WEEK_IN_SECONDS
# Calculate the cutoff time for voting.
# Check to see if the article can still be voted on (we could use the article HASH here, but scores are returned as floats so we dont have to cast it).
	if conn.zscore('time:', article) < cutoff:
		return
# Get the id portion from the article:id identifier.
	article_id = article.partition(':')[-1]
	print("entering article_vote " + article) 
	if conn.sadd('voted:' + article_id, user):
		conn.zincrby('score:', article, VOTE_SCORE)
		conn.hincrby(article, 'votes', 1)

def post_article(conn, user, title, link):
# Generate a new article id. and add the posters-id to it
	article_id = str(conn.incr('article:'))
	voted = 'voted:' + article_id
	conn.sadd(voted, user)
# Start with the posting user having voted for the article, and set the article voting information to automatically expire in a week (we discuss expiration in chapter 3).
	conn.expire(voted, ONE_WEEK_IN_SECONDS)
	now = time.time()
	article = 'article:' + article_id
	conn.hmset(article, {
		'title': title,
		'link': link,
		'poster': user,
		'time': now,
		'votes': 1,
	})
# Create the article hash.
	conn.zadd('score:', {article : VOTE_SCORE})
	conn.zadd('time:', {article : now})
# Add the article to the time and score ordered ZSETs.
	return article_id
