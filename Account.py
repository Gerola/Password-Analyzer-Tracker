#this will have all the account functions
#reading from files, hashing and writing to the files
#and seeing if the file exists

from hashlib import sha256
import os

class Account():

    def __init__(self):
        self.account_name = ""
        self.list_passwords = []
    
    #-------------------Set the name and hash as well---------------------
    def hash_name(self,name):
         #Sort of like a salt
        self.account_name = sha256(name.encode("utf-8")).hexdigest() #Set the name of the account
    #----------------------------------------------------------------------


    def open_files(self):
        directory = os.getcwd()#get cwd
        directory += "/Accounts"
        if(os.path.exists(directory) == 0):#see if the directory is made or not
            os.mkdir(directory)
        #----------------Get whats inside------------------------
        items = os.listdir(directory)#get the items in the directory
        #--------------------------------------------------------
        #See if the account has been made or not
        os.chdir('Accounts')
        found = 0
        for x in items:
            if (x == self.account_name):
                found = 1
                with open(x,'r') as files_name:
                    for a in files_name:
                        self.list_passwords.append(a.replace('\n', ""))     
        
      #  if(found == 0):
       #     with open(self.account_name,'w') as files_name:
        #        files_name.write("")     
        
        os.chdir('..')
            
    def write_to_file(self,password):#write the new password to the file
        pass

    def create_account(self):
        #if the user wants to create an account at the end
        pass    



