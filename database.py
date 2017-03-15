import pymysql

conn = pymysql.connect(host='yamaseiki.cuuhkmqhmrw0.us-west-1.rds.amazonaws.com', port=3306, user='publicapp', passwd='public', db='inventory')

cur = conn.cursor()
cur.execute("SELECT * FROM catagory")

print(cur.description)
print()

for row in cur:
    print(row)

cur.close()
conn.close()