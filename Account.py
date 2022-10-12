#--------------------
#   Matthew Gerola  -
#   Fall 2022       -
#--------------------

from hashlib import sha256
import os

class Account():

    def __init__(self):
        self.account_name = ""
        self.list_passwords = []
    
    #-------------------Set the name and hash as well---------------------#
    def hash_name(self,name):
        if len(name) > 4:
            name += name[0] + name[1] + name[2] #Salt if the name is larger than 4, will probably change this
        self.account_name = sha256(name.encode("utf-8")).hexdigest() #Set the name of the account
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
                
                os.chdir('..')
                return 0 #account was found    

    #--------------------File not found and needs to be created possibly--------------------#
        
        print("Account not found:")
        s = input("Would you like to create one? Y/N: ")
        if s == 'Y':
            with open(self.account_name,'w') as files_name:
                files_name.write("")     
            os.chdir('..')
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
    def create_account(self):
        os.chdir('Accounts')
        items = os.listdir(os.getcwd())#  get the items in the directory
        for x in items:#check to make sure a unique name
            if x == self.account_name:
                print("This name is already taken please choose another.\n")
                os.chdir('..')
                return 1 #Name already taken
        
        with open(self.account_name,'w') as files_name:
                files_name.write("")     
                os.chdir('..')
                return 0
#--------------------------------------------------------#
