#--------------------
#   Matthew Gerola  -
#   Fall 2022       -
#--------------------

import math


class Perceptron():
    def __init__(self):
        #These numbers produced a 98% correct value
        self.feature_vectors = [4.899999999999999, 1.0, -0.20000000000000304, 0.20000000000000046, -0.4999999999999972]
        self.password_vector = [0,0,0,0,0]
        self.different = [0,0,0,0]
        self.special_chars = {'!':1,'@':1,'#':1,'$':1,'%':1,'&':1,'*':1,'(':1,')':1,'.':1,'^':1}
        #----------Feature Vectors----------:
        #length, number of special characters, number of numbers, number of capital letters, number of different characters (lowercase,uppercase,characters,numbers), entropy of password
        self.learning = 0.10 #learning rate of the program 
        
    def training(self):
        classify = 0
        with open("Passwords_Training.txt",'r') as passwords:
            for PW in passwords:
                values = PW.split(',')
                password = values[0]
                p_n = values[1]
                self.get_weights(password)
                x = self.classify()
                if x < 0:
                    classify = -1
                else:
                    classify = 1
                if int(p_n) != classify:
                    self.update_weights(int(p_n))

            
#------------------Actual classification based on the data collected about the password--------------
    def classify(self):
        total = 0
        for x in range(0,5):
            total += self.feature_vectors[x] * self.password_vector[x]
        return total
#----------------------------------------------------------------------------------------------------


    def get_weights(self,password):#given a password classify the password as strong or weak
        self.reset_values()#reset the values
        if len(password) > 20:
            self.password_vector[0] = 1
        for x in password:
            if x.isupper():
                self.different[1] = 1
                self.password_vector[3] += 1
            elif x.islower():
                self.different[0] = 1
            elif x.isdigit():
                self.different[3] = 1
                self.password_vector[2] += 1
            elif x in self.special_chars.keys():
                self.different[2] = 1
                self.password_vector[1] += 1

        total = 0
        for x in self.different:
            if x == 1:
                total += 1
        self.password_vector[4] = total#this is the total number of different characters

#------------------What the program will use to classify the user password------------------
    def user_classify(self,password):
        self.get_weights(password)#get feature vector
        ww = self.classify()#classify based on feature vector
        if ww >= 0:
            return True
        else:
            return False
#-------------------------------------------------------------------------------------------

                
#-----------When the predictions isn't correct-----------------------------
    def update_weights(self,actual_value):#if the classification is wrong then update the weights
        for x in range(0,5):
            self.feature_vectors[x] = self.feature_vectors[x] + (self.learning * actual_value * self.password_vector[x])
#--------------------------------------------------------------------------

#---------------Reset the Values-----------
    def reset_values(self):
        for x in range(0,5):
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
        
        square = math.pow(total,self.password_vector[0])#amount of unique characters to the power of the length of the password
        entropy = math.log2(square) #log 2 of the total characters present
        self.password_vector[5] = entropy#set the entropy into the password vector
#----------------------------------------------------------------------