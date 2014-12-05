import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    #c.execute("""CREATE TABLE orders
     #         (Make TEXT, Model TEXT, Order_Date TEXT)
		#	  """)
	
    #orders_made = [
     #	 ('Ford', 'Taurus', '2014-9-27'),
		#	 ('Ford', 'Taurus', '2014-10-11'),
	#	 ('Ford', 'Prius', '2014-11-20'),
	#		 ('Ford', 'Focus', '2014-1-8'),
	##		 ('Ford', 'Focus', '2014-3-30'),
	#		 ('Honda', 'Senata', '2014-2-28'),
	#		 ('Honda', 'Senata', '2014-5-14'),
     #        ('Honda', 'Senata', '2014-7-22'),
		#	 ('Honda', 'Civic', '2014-9-2'),
		#	 ('Honda', 'Civic', '2014-11-18'),
		#	 ('Honda', 'Civic', '2014-12-25')
		#	 ]
    
    #c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders_made)
	
    c.execute("""SELECT inventory.Quantity, orders.Make, orders.Model,  
	          orders.Order_date FROM inventory, orders WHERE 
			  inventory.Make = orders.Make ORDER BY orders.Order_Date ASC
			  """)
			  
    rows = c.fetchall()
	
    for r in rows:
        print "Make and Model:  " + r[1] + " " + r[2]
        print "Quantity:  " + str(r[0])
        print "Order Date:  " + r[3]		
        print 
		