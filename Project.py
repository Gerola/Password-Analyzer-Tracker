#--------------------
#   Matthew Gerola  -
#   Fall 2022       -
#--------------------

from Account import Account
from Perceptron import Perceptron
from New_Password import New_Password
import os

#-----------------------------------------------------------#
    #Currently this is just full of code that is being tested,
    #Nothing is final in this file yet...
#-----------------------------------------------------------#

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

def user_class():
    global log
    if log: #1 means someone is logged in...
        password = input("Enter the password that you want to use: ")
        if(acc.pass_used(sha256(password.encode("utf-8")).hexdigest())):
            print("This password has already been used")
            input("Press Enter to Continue...")
        per.user_classify(password)
        

def create_account():
    names = input("Name of new account: ")
    hashing = acc.hash_name(names)
#   print(names)
#   print(hashing)
    acc.create_account(hashing)
    
command = {1:user_class,2:create_account,3:login,4:logout,5:quit}#easier calling of functions

def Project():
    acc.check_for_Accounts() #Verify this directory is present

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
        if (s == 2 or s == 3) and log == 0:
            log = 1


        command[s]()

def main():
    Project()
    

if __name__ == "__main__":
    main()