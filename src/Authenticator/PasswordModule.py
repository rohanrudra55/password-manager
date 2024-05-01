import bcrypt
import psycopg2  # for database interaction
from cryptography.fernet import Fernet  # for AES-256 encryption
import secrets
import base64


class Password:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt(self, text):
        encrypted_text = self.fernet.encrypt(text.encode())
        return encrypted_text.decode()

    def decrypt(self, encrypted_text):
        decrypted_text = self.fernet.decrypt(encrypted_text.encode()).decode()
        return decrypted_text

    def generate_hash_and_salt(self, plain_text_password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
        return hashed_password, salt

    def check_hash(self, plain_text_password, stored_hash, stored_salt):
        hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'), stored_salt)
        return hashed_password == stored_hash

    def suggest(self,length=32):
        random_bytes = secrets.token_bytes(length)
        password_string = base64.b64encode(random_bytes).decode('utf-8')
        return password_string

    def validate(self,text):
        unwanted_chars = "!@#$%^&*()"
        min_length = 10
        if len(text) < min_length:
            return False

        for char in unwanted_chars:
            if char in text:
                return False
        return True
