import MySQLdb

# Open database connection
db = MySQLdb.connect("192.168.1.100","abhi","Qwer$099","tutorial")

# prepare a cursor object using cursor() method
cursor = db.cursor()

stocks = [
    ('GOOG', 100, 490.06),
    ('AAPL', 50, 545.76)
]

# Prepare SQL query to INSERT a record into the database.
sql = 'INSERT INTO stock(name,qty,price) VALUES (?,?,?)'

try:
    # Execute the SQL command
    cursor.executemany(sql,stocks)
    # Commit your changes in the database
    db.commit()
except Exception as ex:
   # Rollback in case there is any error
   db.rollback()
   print(ex)

# disconnect from server
db.close()