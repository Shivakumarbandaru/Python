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
	cursor.execute("INSERT INTO " + TABLENAME + " VALUES(" + value + ")", userData)
	connection.commit()
	print("Record added successfully.")

def read():
	records = connection.execute("SELECT * FROM " +  TABLENAME)
	for record in records:
		for x in record:
			print(x, end = " ")
		print("\n")

def update():
	tempId = input("Enter " + fields[0] + " to update the record: ")
	query = cursor.execute("SELECT * FROM " + TABLENAME)
	found = 0
	counter = 1
	for data in query:
		if data[0] == tempId:
			print("Record match is found")
			for x in range(1, len(fields)):
				print(str(counter) + ". " + fields[x])
				counter += 1

			option = int(input("Select one option to update:  "))
			tempData =  input("Enter new " + fields[option] + " : ")
			cursor.execute(" UPDATE " + TABLENAME + " SET " +  fields[option] + " = ? WHERE " + fields[0] + " = ?", (tempData, tempId))
			found = 1
			connection.commit()
			print("Record updated successfully.")
	if found == 0:
		print(fields[0] + " is not found.")


def delete():
	found = 0
	tempId = input("Enter " + fields[0] + " to delete the record: ")
	records = cursor.execute("SELECT * FROM " +  TABLENAME)
	for record in records:
		if record[0] == tempId:
			cursor.execute("DELETE FROM " + TABLENAME + " WHERE " + fields[0] + " = " + tempId)
			found = 1
			connection.commit()
			print("Record deleted successfully")
	if found == 0:
		print(fields[0] + " is not found.")



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
	