from pymongo import MongoClient
import sqlite3
# conn = MongoClient("localhost", 27017)
#
# db = conn.test.student
# current = db.find()
# for values in current:
#     print(values["Name"]+" "+str(values["Id"]))
# print()
# conn.close()

connection = sqlite3.connect("Emp9.db")
cursor = connection.cursor()
# cursor.execute("""Drop table employee;""")
# sql_command="""CREATE TABLE employee(staff_number INTEGER PRIMARY KEY, fname VARCHAR(20), lname VARCHAR(30));"""
#
# cursor.execute(sql_command)
# cursor.execute("""INSERT INTO employee VALUES (1,"PWilliam", "AShakespeare");""")
# cursor.execute("""INSERT INTO employee VALUES (2,"PW", "Kespeare");""")
# cursor.execute("""INSERT INTO employee VALUES (3,"Will", "Peare");""")
#
# connection.commit()
# print("Inserted values")

cursor.execute("Select * from employee")
result = cursor.fetchall()
try:
    fh = open("dataSqlLite.txt", "w")
        for r in result:
            r = list()
