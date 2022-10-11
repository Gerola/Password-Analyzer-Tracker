#--------------------
#   Matthew Gerola  -
#   Fall 2022       -
#--------------------

from Account import Account
from Perceptron import Perceptron
from New_Password import New_Password

#-----------------------------------------------------------#
    #Currently this is just full of code that is being tested,
    #Nothing is final in this file yet...
#-----------------------------------------------------------#

def Project():
    per = Perceptron()#<---
    NP = New_Password()#<--- All the variables needed
    acc0unt = Account()#<---

    s = Account()
    name = input("Enter your name: ")
    s.hash_name(name)
    s.find_Account()
    
    print(s.account_name)
    s = 1
    while(s != 4):
        s = input("1. Enter Password \n2. Find Account\n3. Create Account\n4. Exit\n")
        s = int(s)
        per.training()
        print(per.feature_vectors)
    #if 1 enter input
    #2 find the account to login
    #3 create new account
    #4 leave the program

def main():
    Project()
    

if __name__ == "__main__":
    main()