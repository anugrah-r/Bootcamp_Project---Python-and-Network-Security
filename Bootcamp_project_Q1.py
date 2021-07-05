import hashlib

str = input("Enter the string to be encrypted: \n") #enter the string to be hashed
str_enc = str.encode()                              #Encoding (str_enc is encoded string)
print("encoded :", str_enc)
op = hashlib.md5(str_enc)                           #hashing
opd = op.digest()
print("Hashed string : ", opd)
print("Hexadecimal equivalent : ",op.hexdigest())
