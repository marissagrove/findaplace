import psycopg2
import psycopg2.extras
import pprint

from flask import Flask
app = Flask(__name__)
app.debug= True

pp = pprint.PrettyPrinter(indent=4)

try:
	conn = psycopg2.connect("dbname='findaplace'")
except:
	print "I am unable to connect to the database"

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cur.execute("""SELECT * from places""")

happy_puppies = cur.fetchall()

#print "\n Places:\n"
#for happy_puppy in happy_puppies:
	#pp.pprint (happy_puppy)

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

#pp.pprint(get_places_by_higher_rating(3))

#select * from places order by created_at DESC
#select * from places order by ratings

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/greet")
def hi():
    return "<h1> Hello </h1>!"

@app.route("/places")
def show_places():
	print 'showing places'
	query = """SELECT * from places order by rating ASC"""
	print 'executnig query'
	cur.execute(query)
	print 'executed'
	places = cur.fetchall()
	print 'buliding html string'
	html = """<html>
			  <head> <title> Find a Place </title>
			  </head>
			  <body>
			  <table>
			  <thead>
			  <th>Submitted by</th>
			  <th>Name</th>
			  <th>Location</th>
			  <th>Created at</th>
			  <th>Rating</th>
			  <th>New</th>
			  </thead>

			  <tbody>"""


	for place in places: 
		print 'processing places'
		html = html + "<tr><td>" + str(place['submitted_by'])  + "</td><td>" + str(place['name']) + "</td><td>" + str(place['location']) + "</td><td>" + str(place['created_at']) + "</td><td>" + str(place['rating']) + "</td><td>" + str(place['new']) + "</td></tr>"
 	html = html + "</tbody></body></html>"
 	print 'returning html'
	return html



if __name__ == "__main__":
    print "hit us in your browser"
    app.run()

