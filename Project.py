#--------------------
#   Matthew Gerola  -
#   Fall 2022       -
#--------------------

from Account import Account
from Perceptron import Perceptron
from New_Password import New_Password
import random
import os

#-----------------------------------------------------------#
    #Currently this is just full of code that is being tested,
    #Nothing is final in this file yet...
#-----------------------------------------------------------#

def Project():
    per = Perceptron()#<---
    NP = New_Password()#<--- All the variables needed
    acc = Account()#<---
    command = {1:per.user_classify,2:acc.find_Account,3:acc.create_account,4:login,5:quit}#easier calling of functions
    acc.check_for_Accounts() #Verify this directory is present
    s = 0
    name = "N/A"
    log = 0
    while(1):
        os.system('clear')
        print("Currently logged in as " + name)
        print("----------------------------------")
        s = input("-        1. Test Password        -\n-        2. Find Account         -\n-        3. Create Account       -\n-        4. Login                -\n-        5. Exit                 -\n----------------------------------\n\nInput:")
        if(s != '1' and s != '2' and s != '3' and s != '4' and s != '5'):
            continue #Don't to anything
        s = int(s)
        if (s == 2 or s == 3) and login == 0:
            log = 1


        command[s]()    
        #-------------Testing-------------
        #       if the entropy is high then say the password is good but could be better and then give the suggestions
        #   about what to change


    #if 1 enter input
    #2 find the account to login
    #3 create new account
    #4 leave the program
def quit():
    os.system('clear')
    exit()

def login():
    pass


def main():
    Project()
    

if __name__ == "__main__":
    main()