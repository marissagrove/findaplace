import psycopg2
import psycopg2.extras

try:
	conn = psycopg2.connect("dbname='findaplace'")
except:
	print "I am unable to connect to the database"

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cur.execute("""SELECT * from places""")

def get_place_by_name(name):
	query = """select * from places where name='""" + name + """'"""
	print query
	cur.execute(query)
	place = cur.fetchone()
	return place

#pp.pprint(get_place_by_name('alembic'))

def get_place_by_location(location):
	query = """select * from places where location='""" + location + """'"""
	cur.execute(query)
	place = cur.fetchone()
	return place

#pp.pprint(get_place_by_location('soma'))

def get_place_name_by_location(location):
	query = """select name from places where location='""" + location +"""'"""
	cur.execute(query)
	place = cur.fetchone()
	return place[0]

#pp.pprint(get_place_name_by_location('soma'))

def get_places_by_higher_rating(rating):
	query = """select name from places where rating > """ + str(rating)
	cur.execute(query)
	places = cur.fetchall()
	return places

def login(LoginForm):
	username = username ['username']
	password = password ['password']

def create_place(place):
	username = place ['username'] 
	locationname = place ['locationname']
	location = place ['location']
	description = place ['description']
	rating = place ['rating']
	been_before = place ['new']
	if been_before.lower() == "yes":
		been_before = True 
	else:
		been_before = False
	created_at = place ['date']
	print username + ' ' + locationname + ' ' + location + ' ' + description + ' ' + rating + ' ' + str(been_before) + ' ' + created_at
	sql_query = "insert into places values('" + locationname + "', '" + location + "', '" + description + "', " + str(rating) + "," + str(been_before) + ",'" + created_at + "','" + username + "')"
	print sql_query
	cur.execute("INSERT INTO places (name, location, description, rating, new, created_at, submitted_by) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
			(locationname, location, description, rating, been_before, created_at, username))
	conn.commit()

def find_all():
	query = """SELECT * from places order by rating ASC"""
	cur.execute(query)
	places = cur.fetchall()
	return places 

def hello_module(name):
	print "hello " + name