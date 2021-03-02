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
		connection.commit()
		print("number_of_rows affected =", cursor.rowcount)
		if (cursor.rowcount > 0):
			print("Record added successfully.")
		else: 
			print("Record insertion failed.")

	except Exception as e:
		print("Error occured.", e)
		print("Record insertion failed.")

def read():
	try:
		records = connection.execute("SELECT * FROM " +  TABLENAME)
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
			cursor.execute(" UPDATE " + TABLENAME + " SET " +  fields[option] + " = ? WHERE " + fields[0] + " = ?", (tempData, tempId))
			connection.commit()
			print("number_of_rows affected =", cursor.rowcount)
		else: 
			print("Invalid option.")

	except Exception as e:
		print("Error occured.", e)
		print("Record updation failed.")
	else:
		if (cursor.rowcount > 0):
			print("Record updated successfully.")
		else:
			print("Record updated unsuccessful.")

	
	

def delete():
	tempId = input("Enter " + fields[0] + " to delete the record: ")
	try:
		cursor.execute(" UPDATE " + TABLENAME + " SET " +  fields[-1] + " = ? WHERE " + fields[0] + " = ?", ("0", tempId))
		connection.commit()
		print("number_of_rows affected =", cursor.rowcount)
		if (cursor.rowcount > 0):
			print("Record deleted successfully.")
		else:
			print("Record deletion is not successful.")

	except Exception as e:
		print("Error occured.", e)
		print("Record deletion is not successful.")
		



def exitFromMenu():
	print("Thank you.")
	connection.close()
	exit()


def showMenu():
	while True:
		print("\nChoose one option: ")
		print(open(MENU_FILE).read())
		[create, read, update, delete, exitFromMenu][int(input("Enter your choice: ")) - 1]()

getColumns()
showMenu()	
	
