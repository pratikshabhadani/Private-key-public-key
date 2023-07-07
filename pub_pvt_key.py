import random
def pubkey_gen(key):
    num= random.randint(1, 26)
    os= ""
    for char in key:
        x= ord(char)+num
        if(x>ord("z")): x= x-26
        os+=chr(x)
    return os
def pubkey_verify(key1, key2):
    for i in range(0, 27):
        temp_key=""
        for char in key1:
            x= ord(char)+i
            if(x>ord("z")): x= x-26
            temp_key+=chr(x)
        if(temp_key==key2): return True
    return False
key="ball"
x= int(input("enter 0 for generating a public key and 1 for verifying any key: "))
if(x==0):
    print(pubkey_gen(key))
elif(x==1):
    key1= input("enter public key to verify: ")
    print(pubkey_verify(key1, key))
else:
    print("invalid input")