import psycopg2
import psycopg2.extras

try:
	conn = psycopg2.connect("dbname='findaplace'")
except:
	print "I am unable to connect to the database"

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cur.execute("""SELECT * from users""")

def form(LoginForm):
	username = username ['username']
	password = password ['password']

def login(user):
	username = user['username']
	password = password ['password']
	print username + ' ' + password 
	sql_query = "select username, password from users where username = '" + username + "' and password = '" + password + "'"
	print sql_query
	cur.execute(sql_query)
	results = cur.fetchall()
	
	
