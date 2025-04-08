from cryptography.fernet import Fernet

SECRET_KEY = Fernet.generate_key()
cipher = Fernet(SECRET_KEY)

def encrypt_secret(secret: str) -> str:
    return cipher.encrypt(secret.encode()).decode()

def decrypt_secret(token: str) -> str:
    return cipher.decrypt(token.encode()).decode()