import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sarah315",
    database="testb",
)
u="SELECT name,calories FROM Foods"

cursor = connection.cursor()
cursor.execute(u)

# results1 = cursor.fetchall()
# for row in results1:
#     print(row)



data = cursor.fetchall()
print(data[0][1])
n=40
calorie = (float((data[0][1].split(" "))[0])/100)*40
print(calorie)
print(type(data))

# cursor.close()
# connection.close()
