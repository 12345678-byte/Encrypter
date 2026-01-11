from cryptography.fernet import Fernet
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

def generate(path):
    if not os.path.exists(path) or (os.path.getsize(path) == 0):
        with open(path, 'wb') as file:
            file.write(os.urandom(16))
    with open(path, "rb") as file:
        return file.read()
    
def derive_key(password, salt):
    password = password.encode()
    kdf = PBKDF2HMAC(length=32,salt=salt,iterations=100000,algorithm=hashes.SHA256())
    return base64.urlsafe_b64encode(kdf.derive(password))

def encryptFile(f, key):
    try:
        with open(f,'rb') as file:
            data = file.read()
            fer = Fernet(key)
            data = fer.encrypt(data)
        with open(f, 'wb') as file:
            file.write(data)
        return True
    except Exception:
        return False

def decryptFile(f, key):
    try:
        with open(f,'rb') as file:
            data = file.read()
            fer = Fernet(key)
            data = fer.decrypt(data)
            
        with open(f, 'wb') as file:
            file.write(data)
        return True
    except Exception:
        return False

def processTarget(target, key, mode):
    # Step 1: Gather the files
    files_to_process = []
    
    if os.path.isdir(target):
        for filename in os.listdir(target):
            if filename == 'X.salt': # The Guard
                continue
            full_path = os.path.join(target, filename)
            if os.path.isfile(full_path): # Only process files, skip sub-folders
                files_to_process.append(full_path)
    elif os.path.isfile(target):
        files_to_process.append(target)
    else:
        print("Invalid path!")
        return

    # Step 2: Execute the work
    for file_path in files_to_process:
        if mode == 1:
            success = encryptFile(file_path, key)
            action = "Encrypted"
        else:
            success = decryptFile(file_path, key)
            action = "Decrypted"
            
        if success:
            print(f"✅ {action}: {os.path.basename(file_path)}")
        else:
            print(f"❌ Failed: {os.path.basename(file_path)}")
            
p = 'X.salt' 
salt = generate(p)
password = input("Enter your password: ")
key = derive_key(password,salt)
if key:
    print("Welcome!!")
    f = input("Please enter the file path: ")
    i = int(input("1) Encrypt\n2) Decrypt\nEnter a choice: "))
    processTarget(f,key,mode=i)