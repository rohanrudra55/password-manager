import psycopg2
import TokenModule, PasswordModule
import FaceModule
import warnings


class Connect:
    def __init__(self):
        self.stored_token = 0
        self.stored_secret_key = b''
        self.user_verified = False
        self.stored_email = ''
        self.stored_user_data = []
        self.table_col = 2

    @staticmethod
    def add_user(username, email, password):
        connection = psycopg2.connect(
            dbname="storage",
            user="python_app",
            password="9999",
            host="127.0.0.1"
        )
        cursor = connection.cursor()
        password_auth = PasswordModule

        try:
            hashed_password, salt = password_auth.generate_hash_and_salt(password)
            token = TokenModule.create()
            key = PasswordModule.create_key()
            sql = ("INSERT INTO users (username, password_hash, salt, key, key_token, email) VALUES (%s, %s, %s, %s, "
                   "%s, %s)")
            cursor.execute(sql, (username, hashed_password, salt, key, token, email))
            obj = TokenModule.Token()
            obj.settemplate('cls6789654')
            obj.send_mail(token, email)
            print('Press \'S\' to capture your face in good lighting condition!')
            obj = FaceModule.Biometric()
            obj.create(token)
            connection.commit()
            return True

        except (Exception, psycopg2.Error) as error:
            print(error)

        connection.close()
        return False

    def verify_user_signin(self, username, password):
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
                self.stored_secret_key = result[0][4].tobytes()
                self.stored_token = result[0][5]
                self.stored_email = result[0][6]
                self.user_verified = True
                return True
        except (Exception, psycopg2.Error) as error:
            print(error)
        return False

    def add_user_data(self, username, password, url, note='NA'):
        try:
            connection = psycopg2.connect(
                dbname="storage",
                user="python_app",
                password="9999",
                host="127.0.0.1"
            )
            cursor = connection.cursor()
            sql = """ INSERT INTO user_data (username, password, url, note) VALUES (%s, %s, %s, %s)"""
            password = PasswordModule.encrypt(self.stored_secret_key, password)
            record_to_insert = (username, password, url, note)
            cursor.execute(sql, record_to_insert)
            connection.commit()
            connection.close()
            print("Saved!")
            return True
        except (Exception, psycopg2.Error) as error:
            print(error)
        return False

    def view_stored_data(self):
        try:
            connection = psycopg2.connect(
                dbname="storage",
                user="python_app",
                password="9999",
                host="127.0.0.1"
            )
            cursor = connection.cursor()
            sql = """ SELECT * from user_data"""
            cursor.execute(sql)
            self.stored_user_data = cursor.fetchall()
            # [('rohan', <memory at 0x10fa83880>, 'rr', 'test')]
            if TokenModule.verify(self.stored_email, self.stored_token):
                print("Sites:")
                count = 0
                for row in self.stored_user_data:
                    count = 1 + count
                    print(f'({count}) {row[self.table_col]}')
                connection.commit()
            else:
                connection.rollback()
            connection.close()
        except (Exception, psycopg2.Error) as error:
            print(error)

    def view_stored_password(self, site):
        count = 0
        obj = FaceModule.Biometric()
        obj.verify(self.stored_token)
        for row in self.stored_user_data:
            count = 1 + count
            print('Details:')
            if row[self.table_col] == site:
                print(f'({count})-->\n'
                      f'Username: {row[0]}\n'
                      f'Password: {(PasswordModule.decrypt(self.stored_secret_key, row[1].tobytes())).decode("utf-8")}\n'
                      f'Site: {row[2]}\n'
                      f'Note: {row[3]}')


if __name__ == "__main__":
    obj_1 = Connect()
    obj_1.verify_user_signin('rohanrudra', '5977')
    obj_1.view_stored_data()
    obj_1.view_stored_password('rr')
