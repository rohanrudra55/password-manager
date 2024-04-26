import psycopg2
import hash_gen

def store_encrypted_user_data(encrypted_text):
    conn = psycopg2.connect(
        dbname="storage",
        user="python_app",
        password="9999",
        host="127.0.0.1"
    )
    cur = conn.cursor()
    sql = "INSERT INTO encrypted_data (encrypted_text) VALUES (%s)"
    cur.execute(sql, (encrypted_text,))
    conn.commit()
    conn.close()

def retrieve_and_decrypt_user_data():
    conn = psycopg2.connect(
        dbname="storage",
        user="python_app",
        password="9999",
        host="127.0.0.1"
    )
    cur = conn.cursor()
    cur.execute("SELECT encrypted_text FROM encrypted_data")
    encrypted_data = cur.fetchone()[0]
    decrypted_text = decrypt_text(encrypted_data)
    conn.close()
    return decrypted_text

def store_user(username, plain_text_password, database_connection):

    hashed_password, salt = generate_hash_and_salt(plain_text_password)
    cursor = database_connection.cursor()
    sql = "INSERT INTO users (username, password_hash, salt) VALUES (%s, %s, %s)"
    cursor.execute(sql, (username, hashed_password, salt))
    database_connection.commit()
    cursor.close()


cursor.close()
conn.close()
