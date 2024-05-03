import bcrypt
import psycopg2  # for database interaction
from cryptography.fernet import Fernet  # for AES-256 encryption
import secrets
import base64


def check_hash(plain_text_password, stored_hash, stored_salt):
    hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'), stored_salt)
    return hashed_password == stored_hash


def validate(password):
    # unwanted_chars = "!@#$%^&*()"
    min_length = 10
    if len(password) < min_length:
        return False

    # for char in unwanted_chars:
    #     if char in password:
    # return False
    return True


def suggest(length=32):
    random_bytes = secrets.token_bytes(length)
    password_string = base64.b64encode(random_bytes).decode('utf-8')
    return password_string


def generate_hash_and_salt(plain_text_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
    return hashed_password, salt


def create_key():
    return Fernet.generate_key()


def encrypt(key, text):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text


def decrypt(key, encrypted_text):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text.encode())
    return decrypted_text


# test case

