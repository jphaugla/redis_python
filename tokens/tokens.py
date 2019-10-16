import redis
from check_update_token import check_token,update_token
conn = redis.Redis()

update_token(conn, '666' ,'jphaugla','ItemA')
token=check_token(conn, '666')
print("the new token is " + str(token))
