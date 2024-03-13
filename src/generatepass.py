import secrets
import base64

def generate_strong_password(length=32):
    """Generates a cryptographically secure random password.

    Args:
        length (int, optional): The desired length of the password. Defaults to 32.

    Returns:
        str: The generated random password.
    """

    random_bytes = secrets.token_bytes(length)
    password_string = base64.b64encode(random_bytes).decode('utf-8')
    return password_string

# Example usage
password = generate_strong_password(16)
print(password)