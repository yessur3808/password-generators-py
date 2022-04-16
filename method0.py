import random

# This method uses strings to generate a random password

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbols = "{}[]();*/-_!@#$%^&"

all = lower+upper+num+symbols

def gen_password():
    length = 12
    length = int(input("Enter preferred password length: "))
    
    password = "".join(random.sample(all, length))
    print("Generated Password is ", password)

gen_password()