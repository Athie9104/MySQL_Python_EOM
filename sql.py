
# import mysql.connector
# mydb = mysql.connector.connect(user='lifechoices',
#                                password='@Lifechoices1234',
#                                host='127.0.0.1',
#                                database='LifechoicesOnline',
#                                auth_plugin='mysql_native_password')
# mycursor = mydb.cursor()
# sql = "INSERT INTO Login_out VALUES (%s, curtime())"
# mycursor.execute(sql, [int(input("Enter id\n"))])
# mydb.commit()
#
# mycursor.execute("Select * from Login_out")
# for i in mycursor:
#     print(i)

import mysql.connector
mydb = mysql.connector.connect(user='godwin', password='3494',
host='127.0.0.1', database='lifechoicesonline',
auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
sql = "INSERT INTO Signin VALUES (%s, curtime())"
mycursor.execute(sql, [float(input("Enter id"))])
mydb.commit()

mycursor.execute("Select * from Signin")
for i in mycursor:
    print(i)
