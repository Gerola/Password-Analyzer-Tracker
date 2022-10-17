#--------------------
#   Matthew Gerola  -
#   Fall 2022       -
#--------------------

class New_Password():
    def __init__(self):
        self.passwords = [] #list of new passwords
        self.characters = {'a':4,'c':'(','E':3,'G':6,'L':1,'O':0,'S':5,'T':7,'Z':2,'l':1,8:'&','e':3,'l':1} #dictionary of characters to replace the characters in the old password
        self.extra_words = {0:"m0rn1ng",1:"pop3y3s", 2:"f1sh3rm4n",3:"ph00tb4ll",4:"Un1t3dSaturn",5:"C4lif0nr1a",6:"fromM4rs",7:"1098p1ne4ppl3",8:"thehorsej0ck3y",9:"washhandsd4ily",10:"walkacr0ssstr33t",}
        #extra words to include on the end of the password or in the middle

    def pass_word_creator(self,password):
        op = list(password) #The new password...
        new_pass = ""
        for x in range(0,9): #create 10 passwords for the user to choose from
            for letter in password:
                if letter in self.characters.keys():
                    letter = self.characters[letter]# double check this line...
                elif letter.isdigit():
                    pass
                elif letter.islower():
                    pass
                elif letter.isupper():
                    pass

            op.append(self.extra_words[x])


    #Have the creator get multiple passwords maybe 10 to choose from and select from those...
    