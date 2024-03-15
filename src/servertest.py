import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="storage",
    user="python_app",
    password="9999",
    host="127.0.0.1"
)

sql = "SELECT * FROM users WHERE username = %s AND password = %s"
data = (username, password)

cursor = conn.cursor()

cursor.execute(sql,data)
record = cursor.fetchone()
print("You are connected to - ", record, "\n")

# Close the cursor and connection
cursor.close()
conn.close()
