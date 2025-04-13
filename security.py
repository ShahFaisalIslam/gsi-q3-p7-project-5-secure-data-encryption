# Security module
# Contains functions for encryption/decryption, and secure hashing
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac

ROUNDS : int = 10000

def encrypt(data: str) -> tuple[bytes,bytes]:
    key = Fernet.generate_key()
    encryptor = Fernet(key)
    encrypted_data = encryptor.encrypt(bytes(data,encoding="ascii"))
    return (key,encrypted_data)

def decrypt(encrypted_data: str,key: bytes) -> str:
    decryptor = Fernet(key)
    decrypted_data = decryptor.decrypt(encrypted_data)
    return str(decrypted_data,encoding="ascii")

def gen_secure_hash(passkey: str,salt: bytes) -> bytes:
    return pbkdf2_hmac("sha256",bytes(passkey,"ascii"),salt,ROUNDS)