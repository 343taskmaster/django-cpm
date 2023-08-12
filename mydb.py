import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Afterwards@2213!'
)
#prepare.a.cursor.object
cursorObject = dataBase.cursor()
#prepare.a.databasebvdcf
cursorObject.execute("CREATE DATABASE mydb")
print("ALL DONES")