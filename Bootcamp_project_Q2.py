import hashlib

str = input("Enter the string to be hashed : ")
str_enc = str.encode()
print('Encoded :', str_enc)
print('Select Hash :')
opt = input('1. Blake2b\n2. sha224\n3. sha1\n')
opt = int(opt)
try:
    if opt == 1:
        print('blake2b')
        op = hashlib.blake2b(str_enc)
    elif opt == 2:
        print('sha224')
        op = hashlib.sha224(str_enc)
    elif opt == 3:
        print('sha1')
        op = hashlib.sha1(str_enc)
except:
    print('choose correct option')

opd = op.digest()
print("Hashed string : ", opd)
print("Hexadecimal equivalent : ",op.hexdigest())
