#--------------------
#   Matthew Gerola  -
#   Fall 2022       -
#--------------------

import random
import string
from Perceptron import Perceptron

class New_Password():
    def __init__(self):
        self.passwords = [] #list of new passwords
        self.characters = {'a':4,'c':'(','E':3,'G':6,'L':1,'O':0,'S':5,'T':7,'Z':2,'l':1,8:'&','e':3,'l':1} #dictionary of characters to replace the characters in the old password
        self.numbers = {1:'one', 2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}#have letters instead of number to increase the length of the password
        self.extra_words = {0:"m0rn1ng",1:"pop3y3s", 2:"f1sh3rm4n",3:"ph00tb4ll",4:"Un1t3dSaturn",5:"C4lif0nr1a",6:"fromM4rs",7:"1098p1ne4ppl3",8:"thej0ck3y",9:"washhandsd4ily"}
        #extra words to include on the end of the password or in the middle to also increase the length of the password add more to the password list to increase security



#                                               **************IMPORTANT**************
#-------------Need to check to see if there is only one character in the string then it will make a difference in the new password that
#-------------will be generated
    def password_creator(self,password):
        self.passwords.clear()#reset the values
        length = password
        if len(password) < 10:
            shuffle = random.choices(string.ascii_lowercase,k=10)#Get 10 random numbers that are lowercase
            random.shuffle(shuffle)#shuffle the string into something else if too short
            shuffle_string = "".join(shuffle)
            while len(length) < 10:
                length += shuffle_string
        rands = 0
        new_pass = ""
        check_digits = 0
        for x in range(0,10): #create 10 passwords for the user to choose from
            rands = random.randint(0,1)
          #  print(rands)
            for letter in length:
                rands = random.randint(0,1)
                if letter in self.characters.keys():
                    if rands == 0 :
                        new_pass += (str(self.characters[letter]))
                    else:
                        new_pass += (letter)
                elif letter.isdigit():
                    check_digits = 1
                    if rands == 0:
                        new_pass += str(self.numbers[int(letter)])
                    else:
                        new_pass += str(letter)
                #keep the numbers in the password
                elif letter.islower():
                    if rands == 0:
                        new_pass += (letter.upper())
                    else:
                        new_pass += (letter)
                elif letter.isupper():
                    if rands == 0:
                        new_pass += (letter.lower())
                    else:
                        new_pass += (letter)
                else:
                    new_pass += (str(letter))#Nothing to change then add to the new password
            

            new_pass += self.extra_words[random.randint(0,9)]#add the extra word onto the end of the new password

            # shuffling will help with the real world aspect since this perceptron doesn't know words only number of items in
            #   a password
            if rands == 1:
                op = list(new_pass)
                random.shuffle(op)
                new_pass = "".join(op)
                self.passwords.append(new_pass)
                new_pass = ""
            else:
                self.passwords.append(new_pass)
                new_pass = ""
        
        self.run_new_passwords()
           
    #Have the creator get multiple passwords maybe 10 to choose from and select from those...


#Have the new passwords generated be run through the machine learning vector to classify them as weak or strong
#-----------------------------------------------------
    def run_new_passwords(self):
        classify = Perceptron()
        strong = []
        for x in self.passwords:
            if classify.user_classify(x):
                
                strong.append(x)
                
        self.passwords = strong
#-----------------------------------------------------