from cryptography.fernet import Fernet
import os

def generate(path):
    if not os.path.exists(path) or (os.path.getsize(path) == 0):
        with open(path, 'wb') as file:
                file.write(Fernet.generate_key())
                print("Key created successfully")
        return
    else:
         return
    
def encryptFile(f, key):
    with open(f,'rb') as file:
        data = file.read()
        fer = Fernet(key)
        data = fer.encrypt(data)
        

    with open(f, 'wb') as file:
        file.write(data)

def decryptFile(f, key):
    try:
        with open(f,'rb') as file:

            data = file.read()
            fer = Fernet(key)
            data = fer.decrypt(data)
            

        with open(f, 'wb') as file:
            file.write(data)
    except Exception:
        print("The file might not be encrypted")

p = 'secret.key' 
generate(p)
with open(p, "rb") as file:
    key = file.read()

print("Welcome!!")
f = input("Please enter the file path: ")
i = int(input("1) Encrypt\n2) Decrypt\nEnter a choice: "))
match(i):
    case 1:
        encryptFile(f,key)
    case 2:
        decryptFile(f,key)