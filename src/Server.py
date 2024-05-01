import psycopg2
from Authenticator import PasswordModule


class Bridge:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="storage",
            user="python_app",
            password="9999",
            host="127.0.0.1"
        )
        self.cursor = self.connection.cursor()

    def add_user(self, username, password):
        hashed_password, salt = PasswordModule.Password.generate_hash_and_salt(password)
        sql = "INSERT INTO users (username, password_hash, salt) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (username, hashed_password, salt))
        self.connection.commit()

    def close(self):
        self.connection.close()