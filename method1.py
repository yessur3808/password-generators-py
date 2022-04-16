import random
import array
 
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
 
# combines all the character arrays above to form one array

all = lower+upper+nums+symbols


def gen_password():

    length = int(input("Enter preferred password length: "))

    while(length < 2):
        print('The length you entered is too short... try something more than the number 2')
        length = int(input("Enter preferred password length: "))
 
    rand_upper = random.choice(upper)
    rand_lower = random.choice(lower)
    rand_num = random.choice(nums)
    rand_symbol = random.choice(symbols)
    
    temp_pass = rand_num + rand_upper + rand_lower + rand_symbol

    for x in range(length - 1):
        temp_pass = temp_pass + random.choice(all)
    
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x
            

    print("Generated Password is ",password)


gen_password()