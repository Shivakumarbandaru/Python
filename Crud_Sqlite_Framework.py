import sqlite3
MENU_FILE = "sqlMenu.cfg"
DATABASENAME = "data.db"
connection = sqlite3.connect(DATABASENAME)
cursor = connection.cursor()
TABLENAME = "FRAMEWORK_TABLE"
fields = []


def getColumns():
	rawData = cursor.execute("pragma table_info({})".format(TABLENAME))  #syntax: {}.format(value) //  string.format(var1, var2,...)
	for record in rawData:
		fields.append(record[1])
	if len(fields) == 0:
		print("Table is not found")
		exit(0)
	


def create():
	userData = []
	[userData.append(input("Enter the " + field + ": "))for field in fields]
	value = ""
	for counter in range(len(fields)):
		if counter != len(fields) - 1:
			value += "?,"
		else:
			value += "?"	
	try:		
		cursor.execute("INSERT INTO " + TABLENAME + " VALUES(" + value + ")", userData)
		print("number_of_rows affected =", cursor.rowcount)
		if (cursor.rowcount > 0):
			connection.commit()
			print("Record added successfully.")
		else: 
			print("Record insertion failed.")

	except Exception as e:
		print("Error occured.", e, type)
		print("Record insertion failed.")
		connection.rollback()

def read():
	try:
		records = cursor.execute("SELECT * FROM " +  TABLENAME + " WHERE " + fields[-1] + " = 1")
		for field in fields:
			print(field, end = " ")
		for record in records:
			print("\n")
			for data in record:
				print(data, end = " ")
	except Exception as e:
		print("Error occured.", e)
		print("Record reading is  failed.") 
		

def update():
	tempId = input("Enter " + fields[0] + " to update the record: ")
	counter = 1
	for x in range(1, len(fields) - 1):
		print(str(counter) + ". " + fields[x])
		counter += 1
	try:
		option = int(input("Select one option to update:  "))
		if option > 0 and option < (len(fields) - 1):
			tempData =  input("Enter new " + fields[option] + " : ")
			cursor.execute(" UPDATE " + TABLENAME + " SET " +  fields[option] + " = ? WHERE " + fields[0] + " = ? AND " + fields[-1] + " = 1", (tempData, tempId))
			print("number_of_rows affected =", cursor.rowcount)
			if (cursor.rowcount > 0):
				connection.commit()
				print("Record updated successfully.")
			else:
				print("ID is not found.")
		else: 
			print("Invalid option.")

	except Exception as e:
		print("Error occured.", e)
		print("Record updation failed.")
		connection.rollback()
		
	

def delete():
	tempId = input("Enter " + fields[0] + " to delete the record: ")
	try:
		cursor.execute(" UPDATE " + TABLENAME + " SET " +  fields[-1] + " = ? WHERE " + fields[0] + " = ?", ("0", tempId))
		print("number_of_rows affected =", cursor.rowcount)
		if (cursor.rowcount > 0):
			connection.commit()
			print("Record deleted successfully.")
		else:
			print("ID is not found.")

	except Exception as e:
		print("Error occured.", e)
		print("Record deletion is not successful.")
		connection.rollback()



def search():
	tempId = input("Enter " + fields[0] + " to search the record: ")
	try:
		records = cursor.execute("SELECT * FROM " +  TABLENAME + " WHERE " + fields[0] + " = " + tempId)
		for field in fields:
			print(field, end = " ")
		for record in records:
			print("\n")
			for data in record:
				print(data, end = " ")

	except Exception as e:
		print("Error occured.", e)



def exitFromMenu():
	print("Thank you.")
	connection.commit()
	connection.close()
	exit()


def showMenu():
	while True:
		print("\nChoose one option: ")
		print(open(MENU_FILE).read())
		option = int(input("Enter your choice: ")) 
		if option > 0:
			try:
				[create, read, update, delete, search, exitFromMenu][option - 1]()
			except Exception as e:
				print("Error occured.", e)


getColumns()
showMenu()	
	
