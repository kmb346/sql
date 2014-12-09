import sqlite3

with sqlite3.connect("Cars.db") as connection:
    c = connection.cursor()
	
	# fetch the make, model and quantity
    c.execute("SELECT * FROM Inventory")
	
    rows = c.fetchall()
	# print the values for the make, model and quantity 
    for r in rows:
        print "\nMake and Model:  " + r[0] + " " + r[1]
        print "Quantity:  " + str(r[2])
		
        c.execute("SELECT count(Order_date) FROM orders WHERE Make=? and Model=?",
		           (r[0], r[1]))
        count = c.fetchone()
		
        print "Order Count:  " + str(count[0])
        	   