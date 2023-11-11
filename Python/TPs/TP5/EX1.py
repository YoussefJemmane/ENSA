import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="yous1/2*3-LOLIl",
    database="mydatabase"
)

cursor = mydb.cursor()


cursor.execute("DROP DATABASE IF EXISTS mydatabase; CREATE DATABASE mydatabase;")

cursor.execute(" SHOW DATABASES ")

for x in cursor:
    print(x)

cursor.execute("""
    CREATE TABLE customers(
        name VARCHAR(255),
        address VARCHAR(255)
    )
""")

cursor.execute("""
    SHOW TABLES;
""")

cursor.execute("""
    ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY
""")

insert_client = """ INSERT INTO customers (name,address) VALUES (%s,%s) """
val = ("Youssef","Ecole Drissia, Rue A, Idrissia 2")

cursor.execute(insert_client,val)
mydb.commit()
print(cursor.rowcount,"record inserted")


insert_client = """ INSERT INTO customers (name,address) VALUES (%s,%s) """
val = [("Youssef","Ecole Drissia, Rue A, Idrissia 2"),("Ayoub","Derb Sadni")]

cursor.executemany(insert_client,val)
mydb.commit()
print(cursor.rowcount,"record inserted , ID : ", cursor.lastrowid)

cursor.execute(""" SELECT * FROM customers Where address ='Derb Sadni'""")
customers = cursor.fetchall()

for customer in customers:
    print(customer)

cursor.execute(""" SELECT * FROM customers WHERE address LIKE '%d%'""")
customers = cursor.fetchall()

for customer in customers:
    print(customer)

afficher = """ SELECT * FROM customers WHERE address = %s ORDER BY id DESC"""
val = ("Derb Sadni",)
cursor.execute(afficher,val)
customers = cursor.fetchall()

for customer in customers:
    print(customer)

