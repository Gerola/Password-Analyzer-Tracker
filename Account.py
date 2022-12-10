#--------------------
#   Matthew Gerola  -
#   Fall 2022       -
#--------------------

from hashlib import sha512
import os

class Account():
    def __init__(self):
        self.account_name = "N/A"
        self.list_passwords = []
    
#-------------------Set the name and hash as well---------------------#
    def hash_name(self,name):
        list_salts = ["1234","Tomorrow","Today","789USA"]#Salts for the user accounts to make it harder to solve the hashes
        if len(name) % 4 == 0:
            name += list_salts[3]
        elif len(name) % 3 == 0:
            name += list_salts[2]
        elif len(name) % 2 == 0:
            name += list_salts[1]
        else:
            name += list_salts[0]
        return sha512(name.encode("utf-8")).hexdigest() #Set the name of the account
#----------------------------------------------------------------------#

#--------------------See if the Accounts directory is present or Not---------------#
    def check_for_Accounts(self):
        directory = os.getcwd()#get cwd
        directory += "/Accounts"
        if(os.path.exists(directory) == 0):#see if the directory is made or not
            os.mkdir(directory)
#----------------------------------------------------------------------------------#

#------------------See if the account is present in the Accounts directory-------------------#
    def find_Account(self):

        os.chdir('Accounts')
        #----------------Get whats inside------------------------
        items = os.listdir(os.getcwd())#  get the items in the directory
        #--------------------------------------------------------
        #See if the account has been made or not
        for x in items:
            if (x == self.account_name):
                with open(x,'r') as files_name:
                    for a in files_name:
                        self.list_passwords.append(a.replace('\n', ""))
                
                print("Account was found\n")
                input("Press Enter to continue...")
                os.chdir('..')
                return 0 #account was found    

#--------------------File not found and needs to be created possibly--------------------#
        
        print("Account not found:")
        s = 'O'
        while(s != 'N' and s != 'Y'):
            s = input("Would you like to create one? Y/N: ")    
        if s == 'Y':
            os.chdir('..')
            self.create_account(self.account_name)  
            return 0 #Account created

        else:
            os.chdir('..')
            return 1 #No account was made

#-----------------Check to see if the password has been used by this person already-----#
    def pass_used(self,password):
        for x in self.list_passwords:
            if x == password:
                return 1 #Found
        return 0 #Not found

#-----------------Write the new password to the user file--------------#
    def write_to_file(self,password):
        #write the new password to the file
        os.chdir('Accounts')
        
        with open (self.account_name, 'a+') as account_file:
            account_file.write(password)#Write new password
            account_file.write('\n')
        
        os.chdir('..')#go back
#---------------------------------------------------------------------#


#---------------Making a new Account---------------------#
    def create_account(self,name):
        os.chdir('Accounts')
        items = os.listdir(os.getcwd())#  get the items in the directory
        for x in items:#check to make sure a unique name
            if x == name:
                print("This name is already taken please choose another.\n")
                input("Press enter to contiue...")
                os.chdir('..')
                return 1 #Name already taken
        
        with open(name,'w') as files_name:
                files_name.write("")     
                os.chdir('..')
                input("Account successfully created...")
                return 0
#--------------------------------------------------------#