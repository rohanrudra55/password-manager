import psycopg2
from Authenticator import PasswordModule
from Authenticator import TokenModule


class Connect:
    def __init__(self):
        self.token = 0
        self.secret_key = b''
        self.verified = False

    @staticmethod
    def add_user(username, password='0123456789'):
        connection = psycopg2.connect(
            dbname="storage",
            user="python_app",
            password="9999",
            host="127.0.0.1"
        )
        cursor = connection.cursor()
        password_auth = PasswordModule

        if len(username) > 45:
            print("Username should contains 45 characters!")
            return False

        if not password_auth.validate(password):
            print("Password should contains 10 characters!")
            return False
        try:
            hashed_password, salt = password_auth.generate_hash_and_salt(password)
            token = TokenModule.create()
            key = PasswordModule.create_key()
            sql = "INSERT INTO users (username, password_hash, salt, key, key_token) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (username, hashed_password, salt, key, token))
            connection.commit()
            return True

        except (Exception, psycopg2.Error) as error:
            print(error)

        connection.close()
        return False

    def verify_user(self, username, password):
        # password_auth = PasswordModule
        try:
            connection = psycopg2.connect(
                dbname="storage",
                user="python_app",
                password="9999",
                host="127.0.0.1"
            )
            cursor = connection.cursor()
            sql = "SELECT * FROM users WHERE username = %s"
            cursor.execute(sql, (username,))
            connection.commit()
            result = cursor.fetchall()
            connection.close()
            if PasswordModule.check_hash(password, result[0][2].tobytes(), result[0][3].tobytes()):
                self.secret_key = result[0][4].tobytes()
                self.token = result[0][5]
                self.verified = True
                return True
            else:
                print('Invalid Password')
        except (Exception, psycopg2.Error) as error:
            print(error)
        return False

    def add_credentials(self, password, user_email, username, url, app_name):
        try:
            connection = psycopg2.connect(
                dbname="storage",
                user="python_app",
                password="9999",
                host="127.0.0.1"
            )
            cursor = connection.cursor()
            sql = """ INSERT INTO credentials (password, email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
            password = PasswordModule.encrypt(self.secret_key, password)
            record_to_insert = (password, user_email, username, url, app_name)
            cursor.execute(sql, record_to_insert)
            connection.commit()
            connection.close()
        except (Exception, psycopg2.Error) as error:
            print(error)

# Test Cases
# print(Server.add_user('test', '6296140248'))
# print(verify_user('test', '6296140248'))
