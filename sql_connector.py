import mysql.connector
import time
import datetime


ts = time.time()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="facial_recognition"
    


try:
    mycursor.execute("""INSERT into user_name (time,name) values(%s,%s)""",(timestamp,id))
    mycursor.commit()

except:
    mydb.rollback()

mycursor.close()

    