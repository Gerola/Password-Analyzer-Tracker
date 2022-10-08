#--------------------
#   Matthew Gerola  -
#   Fall 2022       -
#--------------------

import math

#Start on Perceptron and working on reading from a file...

class Perceptron():
    def __init__(self):
        self.feature_vectors = [0,0,0,0,0,0]
        self.password_vector = [0,0,0,0,0,0]
        self.different = [0,0,0,0]
        self.special_chars = {'!':1,'@':1,'#':1,'$':1,'%':1,'&':1,'*':1,'(':1,')':1,'.':1} #dictionary of characters to replace the characters in the old password
        #----------Feature Vectors----------:
        #length, number of characters, number of numbers,
        #number of capital letters, number of different characters (lowercase,uppercase,characters,numbers), entropy
        self.learning = 0.25 #learning rate of the program 
       

    def training(self):
        #Work on this part of the program to read in the password and the corresponding value...
        classify = 0
        with open("Passwords_Training.txt",'r') as passwords:
            for PW,where in passwords:
                self.get_weights(PW)
                x = self.classify()
                if x < 0:
                    classify = -1
                else:
                    classify = 1
                if where != classify:
                    self.update_weights(where)
            
                self.reset_values()

            
#------------------Actual classification based on the data collected about the password--------------
    def classify(self):
        total = 0
        for x in range(0,6):
            total += self.feature_vectors[x] * self.password_vector[x]
        
        return x
#----------------------------------------------------------------------------------------------------


    def get_weights(self,password):#given a password classify the password as strong or weak
        self.password_vector[0] = len(password)#The total length of the password
        for x in password:
            if x.isupper():
                self.different[1] = 1
              #  print("U")
                self.password_vector[3] += 1
            elif x.islower():
                self.different[0] = 1
               # print("L")
            elif x.isdigit():
                self.different[3] = 1
                #print("D")
                self.password_vector[2] += 1
            elif x in self.special_chars.keys():
                self.different[2] = 1
                #print("C")
                self.password_vector[1] += 1
            
        total = 0
        for x in self.different:
            if x == 1:
                total += 1
        self.password_vector[4] = total#this is the total number of different characters
        self.calulate_entropy()


                
#-----------When the predictions isn't correct-----------------------------
    def update_weights(self,actual_value):#if the classification is wrong then update the weights
        for x in range(0,6):
            self.feature_vectors[x] = self.feature_vectors[x] + (self.learning * actual_value * self.password_vector[x])
#--------------------------------------------------------------------------

#---------------Reset the Values-----------
    def reset_values(self):
        for x in range(0,6):
            self.password_vector[x] = 0

        for y in range(0,4):
            self.different[y] = 0
#-----------------------------------------

#-------------------Calculate the Entropy of the Password--------------
    def calulate_entropy(self):
        total = 0
        if self.different[0] == 1:
            total += 26 #lower case letters
        if self.different[1] == 1:
            total += 26 #upper case letters
        if self.different[3] == 1:
            total += 10 #numbers
        
        entropy = math.log2(total) #log 2 of the total characters present
        self.password_vector[5] = entropy#set the entropy into the password vector
        
#----------------------------------------------------------------------