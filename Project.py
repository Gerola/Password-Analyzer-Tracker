#--------------------
#   Matthew Gerola  -
#   Fall 2022       -
#--------------------

from Account import Account
from Perceptron import Perceptron
from New_Password import New_Password
from hashlib import sha256
import os

#-----------------------------------------------------------#
    #Currently this is just full of code that is being tested,
    #Nothing is final in this file yet...
#-----------------------------------------------------------#

#Run Training one more time...
#Something is wrong with the Perceptron functions????


s = 0
name = "N/A"
log = 0
per = Perceptron()#<---
NP = New_Password()#<--- All the variables needed
acc = Account()#<---

def quit():
    os.system('clear')
    exit()

def login():
    global name 
    name = input("Username: ")
    acc.account_name = acc.hash_name(name)
    if (acc.find_Account() == 1):
        name = "N/A"
        return
    global log
    log = 1    
    
def logout():
    global log
    global name
    acc.account_name = ""   #Don't write to anything...
    name = "N/A" #No name logged in...
    log = 0 #indicate no loggin present...
    input("Successfully logged out\nPress enter to continue:")

#--------------Work on this--------------
def user_class():
    global log
    if log: #1 means someone is logged in...
        password = input("Enter the password that you want to use: ")
        if(acc.pass_used(sha256(password.encode("utf-8")).hexdigest())):
            print("This password has already been used")
            input("Press Enter to Continue...")
            return
        
        value = per.user_classify(password)
        if value == True:
            input("This is a strong password\nPress Enter to continue")
            output = 'A'
            while output != 'Y' and output != 'N':
                output = input("Do you want to use this password? (Y/N)")
            if output == 'Y':
                print("Ok, this password will be written to your file\n")
                acc.write_to_file(password)
            else:
                input("Ok, this password will not be written to your file")
            return
        else:
            user_i = -1
            input("This is a weak password\nPress Enter to continue")
            NP.password_creator(password)
            print("Here are the new passwords generated from the password given:\n")
            for x in range(0,len(NP.passwords)):
                print(str(x+1) + ": " + NP.passwords[x-1])
            print("Please choose from the given passwords\n")
            high = ord(str(len(NP.passwords)-1))
            while user_i < 47 or user_i > high + 1:#Look this over
                user_i = input("What password do you want to user?")
                user_i = ord(user_i)
            
            print(user_i)
            print(high + 1)
            print(chr(user_i))
            place = int(chr(user_i))
            print(place)
            place = place - 1
            values = NP.passwords[place - 1]
            print(place)
            print(len(NP.passwords))
            input("Ok, "+ values +" will be written to your file")
            acc.write_to_file(sha256(NP.passwords[place-1].encode("utf-8")).hexdigest())
            return
    else:
        value = per.user_classify(password)

def create_account():
    names = input("Name of new account: ")
    hashing = acc.hash_name(names)
#   print(names)
#   print(hashing)
    acc.create_account(hashing)
    
command = {1:user_class,2:create_account,3:login,4:logout,5:quit}#easier calling of functions

def Project():
    acc.check_for_Accounts() #Verify this directory is present to save the passwords

    while(1):
        global log
        global s
        global name
        os.system('clear')
        print("Currently logged in as " + name)
        print("----------------------------------")
        s = input("-        1. Test Password        -\n-        2. Create Account       -\n-        3. Login                -\n-        4. Logout               -\n-        5. Exit                 -\n----------------------------------\n\nInput:")
        if(s != '1' and s != '2' and s != '3' and s != '4' and s != '5'):
            continue #Don't to anything
        s = int(s)
        if log == 1 and s == 3:
                print("Already logged in...")
                input("Press Enter to Contiue")
                continue

        command[s]()

def main():
    Project()
    

if __name__ == "__main__":
    main()