#--------------------
#   Matthew Gerola  -
#   Fall 2022       -
#--------------------

from Account import Account
from Perceptron import Perceptron
from New_Password import New_Password
from hashlib import sha512
import os


s = 0
name = "N/A" #Name of the account
log = 0 #logged in or not
per = Perceptron()#<---
NP = New_Password()#<---
acc = Account()#<---

def quit():#Quit the program
    os.system('clear')
    exit()

def login():#Login to an account
    global name #name
    name = input("Username: ") #Get the username of the account
    acc.account_name = acc.hash_name(name)#hash the name
    if (acc.find_Account() == 1):#Make sure a unique name
        name = "N/A"
        return
    global log
    log = 1   #Account is logged in now 
    
def logout():
    global log
    global name
    if log != 1:#make sure logged in
        print("Not currently logged in\n")
        input("Press Enter to continue...\n")
        return
    acc.account_name = ""   #Don't write to anything now
    acc.list_passwords = [] #make the list of passwords nothing
    name = "N/A" #No name logged in...
    log = 0 #indicate no loggin present...
    input("Successfully logged out\nPress enter to continue:")#Tell the user they are logged out

def user_class():
    global log
    global name
    if log: #1 means someone is logged in...
        password = input("Enter the password that you want to use: ")
        if password.isspace() or password == "":#the user just hit enter or spaces
            return
        if(acc.pass_used(sha512(password.encode("utf-8")).hexdigest())): #check to make sure hasn't been used before
            print("This password has already been used")
            input("Press Enter to Continue...")
            return
        
        value = per.user_classify(password)#strong password or not
        if value == True:#This is a strong password
            input("This is a strong password\nPress Enter to continue")
            output = 'A'
            while output != 'Y' and output != 'N':#ask if they want to use this password
                output = input("Do you want to use this password? (Y/N)")
            if output == 'Y':#Tell them it will be written to their file
                input("Ok, "+ name+ ", " + password +" will be written to your file")
                acc.write_to_file(sha512(password.encode("utf-8")).hexdigest())
                acc.list_passwords.append(sha512(password.encode("utf-8")).hexdigest())
            else:
                input("Ok, this password will not be written to your file")#Else nothing happens
            return
        else:#Weak password was used and suggestions need to be made
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
            
            place = int(chr(user_i))
            place = place - 1
            values = NP.passwords[place - 1]
            input("Ok, "+ name+ ", " + values +" will be written to your file")
            acc.write_to_file(sha512(NP.passwords[place-1].encode("utf-8")).hexdigest())
            acc.list_passwords.append(sha512(NP.passwords[place-1].encode("utf-8")).hexdigest())
            return
    else:#No user is logged in
        password = input("Enter the password that you want to use: ")
        if password.isspace() or password == "":#the user just hit enter or spaces
            return
        value = per.user_classify(password)
        if value == True:
            print("This is a strong password\n")
            input("Press enter to continue...")
        else:
            print("This is a weak password, its best not to use\n")
            input("Press enter to continue...")

#Create an account to be used
def create_account():
    names = input("Name of new account: ")
    hashing = acc.hash_name(names)
    acc.create_account(hashing)
    
command = {1:user_class,2:create_account,3:login,4:logout,5:quit}#easier calling of functions

#what will be run when the program starts
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
    

if __name__ == "__main__":
    Project()
