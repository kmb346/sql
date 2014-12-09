import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    sql = {"Ford Taurus": "SELECT count(make) FROM orders WHERE Model= 'Taurus'",
	       "Ford Prius": "SELECT count(make) FROM orders WHERE Model= 'Prius'",
		   "Ford Focus": "SELECT count(make) FROM orders WHERE Model= 'Focus'",
		   "Honda Senata": "SELECT count(make) FROM orders WHERE Model= 'Senata'",
		   "Honda Civic": "SELECT count(make) FROM orders WHERE Model = 'Civic'"
		   }
		   
    for keys, values in sql.iteritems():
	
        c.execute(values)
		
        result = c.fetchone()
		
        print keys + ":  " + str(result[0])