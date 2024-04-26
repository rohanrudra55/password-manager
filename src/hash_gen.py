import bcrypt
import psycopg2  # for database interaction
from cryptography.fernet import Fernet  # for AES-256 encryption

key = Fernet.generate_key()
fernet = Fernet(key)

def encrypt_text(text):
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text.decode()

def decrypt_text(encrypted_text):
    decrypted_text = fernet.decrypt(encrypted_text.encode()).decode()
    return decrypted_text


def generate_hash_and_salt(plain_text_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
    return hashed_password, salt

def generate_hash_and_check(plain_text_password, stored_hased, stored_salt):
    hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'),stored_salt)
    return hashed_password == stored_hased
