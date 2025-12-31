from cryptography.fernet import Fernet
import os
p = 'secret.key'
def generate(path):
    if not os.path.exists(path) or (os.path.getsize(path) == 0):
        with open(path, 'wb') as file:
                file.write(Fernet.generate_key())
                print("Key created successfully")
        return
    else:
         return
    
generate(p)

with open(p, "rb") as file:
    key = file.read()
print(key)