import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='publicapp', password='public', host='yamaseiki.cuuhkmqhmrw0.us-west-1.rds.amazonaws.com', port='3306', database='inventory')

cursor = mariadb_connection.cursor()

print("Done")
input()