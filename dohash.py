from SHA256 import sha256 as sha
from random import randint
hashed = 0
hashes = []
text = open("myhashes.txt","w+")
text.close()
read = open("myhashes.txt","r")
hashed = read.__hash__()
print(hashed)
read.close()
text = open("myhashes.txt","w+")
for i in range(200):
    hashed = sha(hashed)
    print(hashed)
    text.write(f"{i+1}:{hashed}\r")
    hashes.append(hashed)
    
text.close()
print(hashes)
print(sha("no")-sha("no"))
endstop = input("Done")
