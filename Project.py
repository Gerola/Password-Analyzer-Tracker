#   Matthew Gerola
#   Fall 2022

from Account import Account
from Perceptron import Perceptron
from New_Password import New_Password
#from New_Password import Password

def Project():
    find = {}
    s = Account()
    name = input("Enter your name: ")
    s.hash_name(name)
    s.open_files()
    
    print(s.account_name)
    s = 1
    while(s != 4):
        s = input("1. Enter Password \n2. Create Account\n3. Find Account\n4. Exit\n")
        s = int(s)



def main():
    Project()
    

if __name__ == "__main__":
    main()