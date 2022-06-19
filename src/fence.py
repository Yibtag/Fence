#################################
#            Fence              #
#          -v: 1.0.0            #
#            Yibtag             #
#################################

#################################
#           Imports             #
#################################

import os
import sys
from cryptography.fernet import Fernet

#################################
#           Constants           #
#################################

CONFIG_PATH = os.path.join(os.getenv("APPDATA") + "\\feance")
KEY_PATH = os.path.join(CONFIG_PATH + "\\config.key")

#################################
#           Classes             #
#################################

class Error:
    def __init__(self, message: str):
        self.message = message

#################################
#           Methods             #
#################################

def getKey(arg: str):
    if not os.path.isdir(CONFIG_PATH):
        os.mkdir(CONFIG_PATH)

    if os.path.isfile(KEY_PATH):
        with open(KEY_PATH, "r+") as f:
            temp = f.read()
            if temp != None:
                return temp
            else:
                return Error("curropt file")
    else:
        with open(KEY_PATH, "w+") as f:
            key = Fernet.generate_key()
            f.write(key.decode("utf-8"))
            return key.decode("utf-8")

def encrypt(file: str, key: bytes):
    if file == None or key == None:
        return Error("missing args")

    if os.path.isfile(file):
        with open(file, "rb") as f:
            content = f.read()
            encrypted_content = Fernet(bytes(key, encoding='utf8')).encrypt(content)
        with open(file, "wb") as f:
            f.write(encrypted_content)
    else:
        return Error("invalid file")

def decrypt(file: str, key: bytes):
    if file == None or key == None:
        return Error("missing args")
    
    if os.path.isfile(file):
        with open(file, "rb") as f:
            content = f.read();
            decrypted_content = Fernet(key).decrypt(content)
        with open(file, "wb") as f:
            f.write(decrypted_content)
    else:
        return Error("invalid file")

#################################
#           Arguments           #
#################################

if sys.argv.__len__() > 1:
    if sys.argv[1] == "-e":
        if sys.argv.__len__() > 2:
            if sys.argv[2] != None:
                error = encrypt(sys.argv[2], getKey(sys.argv[0]));
                if error != None:
                    print(error.message)
            else:
                print(Error("file not provided").message)
        else:
                print(Error("file not provided").message)
    elif sys.argv[1] == "-d":
        if sys.argv.__len__() > 2:
            if sys.argv[2] != None:
                error = decrypt(sys.argv[2], getKey(sys.argv[0]))
                if error != None:
                    print(error.message)
            else:
                print(Error("file not provided").message)
        else:
                print(Error("file not provided").message)
else:
    print("""
    +---------Fence---------+
    |   -e <file>: encrypt  |
    |   -d <file>: decrypt  |
    +-----------------------+
    """)