import sqlite3

connection = sqlite3.connect("newnum.db")

c = connection.cursor()

	
#  display options to user
prompt = """
    Select an option:
    1. average
    2. maximum
    3. minimum
    4. add
    5. close 
	"""	   
	
	
# get user input and loop until valid selection is entered
while True:
    choice = raw_input(prompt)
    
    # check if valid selection    
    if choice in set(["1", "2", "3", "4"]):
	
        sql = {1: "avg", 2: "max", 3: "min", 4: "sum"}[int(choice)]
        
        c.execute("SELECT {}(num) FROM numbers".format(sql))

        output = c.fetchall()
        
        print sql + ":  %f" % output[0]	
    
    elif choice == "5":
        print "Exit"
        break
   
	
