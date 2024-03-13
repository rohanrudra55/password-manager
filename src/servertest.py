import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="primarydb",
    user="alpha",
    password="",
    host="localhost"
)

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Execute a SQL query
cursor.execute("")

# Fetch result
record = cursor.fetchone()
print("You are connected to - ", record, "\n")

# Close the cursor and connection
cursor.close()
conn.close()
