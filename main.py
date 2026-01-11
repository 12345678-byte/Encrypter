import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def get_or_create_salt(path):
    """Ensures a 16-byte salt exists at the given path and returns it."""
    if not os.path.exists(path) or (os.path.getsize(path) == 0):
        with open(path, 'wb') as file:
            file.write(os.urandom(16))
    
    with open(path, "rb") as file:
        return file.read()
    
def derive_key(password, salt):
    """Derives a 32-byte URL-safe key from a password using PBKDF2."""
    password_bytes = password.encode()
    kdf = PBKDF2HMAC(
        length=32,
        salt=salt,
        iterations=100000,
        algorithm=hashes.SHA256()
    )
    # Fernet keys must be base64 encoded
    return base64.urlsafe_b64encode(kdf.derive(password_bytes))

def encrypt_file(file_path, key):
    """Encrypts a single file using the provided key."""
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
        return True
    except Exception:
        return False

def decrypt_file(file_path, key):
    """Decrypts a single file. Returns False if key is incorrect or file corrupted."""
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(data)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
        return True
    except Exception:
        return False

def process_target(target, key, mode):
    """Identifies if target is file or folder and processes accordingly."""
    files_to_process = []
    
    # 1. Gather relevant files
    if os.path.isdir(target):
        for filename in os.listdir(target):
            if filename == 'X.salt': # Skip the key-making ingredient
                continue
            full_path = os.path.join(target, filename)
            if os.path.isfile(full_path):
                files_to_process.append(full_path)
    elif os.path.isfile(target):
        files_to_process.append(target)
    else:
        print("❌ Invalid path! Please check the folder or file name.")
        return

    # 2. Execute the work
    print(f"\n--- Starting {'Encryption' if mode == 1 else 'Decryption'} ---")
    for file_path in files_to_process:
        if mode == 1:
            success = encrypt_file(file_path, key)
            action = "Encrypted"
        else:
            success = decrypt_file(file_path, key)
            action = "Decrypted"
            
        status_icon = "✅" if success else "❌"
        print(f"{status_icon} {action}: {os.path.basename(file_path)}")

# --- Execution ---
if __name__ == "__main__":
    SALT_FILE = 'X.salt' 
    salt = get_or_create_salt(SALT_FILE)

    print("--- 🛡️ FILE SHIELD: Python Security Utility ---")
    password = input("Enter Master Password: ")
    key = derive_key(password, salt)

    target_path = input("Enter file or folder path: ")
    print("\nSelect Action:")
    print("1) Encrypt folder/file")
    print("2) Decrypt folder/file")
    
    try:
        choice = int(input("Selection: "))
        process_target(target_path, key, mode=choice)
    except ValueError:
        print("❌ Please enter a number (1 or 2).")