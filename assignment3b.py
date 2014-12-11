import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
	
    choices = {'1.  ': 'average',
	           '2.  ': 'maximum',
			   '3.  ': 'minimum',
			   '4.  ': 'add',
			   '5.  ': 'close' 
			   }
			   
    for keys, values in choices:
        print keys + values
		
    choice = raw_input("Choose an option:  ")
	
    if choice.lower() == 'average':
        c.execute("SELECT avg(num) FROM Numbers")
    elif choice.lower() =='maximum':
        c.execute("SELECT max(num)FROM Numbers")
    elif choice.lower() =='minimum':
        c.execute("SELECT min(num)FROM Numbers")
    elif choice.lower() =='add':
        c.execute("SELECT sum(num)FROM Numbers")
    else choice.lower() =='close':
        break 
    
    result = c.fetchone()
	
    print "The result is:  " + str(result)
	
        
		