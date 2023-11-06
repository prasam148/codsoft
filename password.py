#Random password generator
import string 
import random

if __name__=="__main__":
    password=[]
    password= list(string.ascii_lowercase+string.ascii_uppercase+string.punctuation+string.digits)
    #print(password)
    
len = input("Enter password length: \n")
random.shuffle(password)
if len.isdigit() == True:
        len = int(len)
        print("Your Generated password is: ")
        print("".join(password[0:len]))
else:
        print("Please enter only digits (dont enter negative integers or string values)")
        
        

    