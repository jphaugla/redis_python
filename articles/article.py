import redis
from post_vote_article import post_article,article_vote
from get_articles import get_articles, get_group_articles
from add_remove_groups import add_remove_groups
conn = redis.Redis()

# post_article(conn, 'jphaugla', 'what a great title', 'link1')
newarticle=post_article(conn, 'jphaugla', 'another great title', 'link2')
print("the new article is " + newarticle)
# article_vote(conn, 'jphaugla', 'article:4')
# article_vote(conn, 'jphaugla', 'article:' + newarticle)
# articles = get_articles(conn, 1, 'time:')
# print(*articles, sep = "\n")
# add_remove_groups(conn, newarticle, to_add=['default','latest'])
articles = get_group_articles(conn,'default',1)
print(*articles, sep = "\n")
