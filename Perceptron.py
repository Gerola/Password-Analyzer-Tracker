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
        self.special_chars = {'!':1,'@':1,'#':1,'$':1,'%':1,'&':1,'*':1,'(':1,')':1,'.':1,'^':1}
        #----------Feature Vectors----------:
        #length, number of special characters, number of numbers, number of capital letters, number of different characters (lowercase,uppercase,characters,numbers), entropy of password
        self.learning = 0.10 #learning rate of the program 
        
        #I took out the entropy and found it generalized the information better than with the entropy involved in the classifiying process
        #will print out the entropy just to show the user what the value is
    
    def training(self):
        classify = 0
        co = 0
        to = 0
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
                    to+= 1
                else:
                    #print("CORRECT")
                    to+=1
                    co+=1
                
        print(str(co) + "/" + str(to))
        print(str(co/to))

            
#------------------Actual classification based on the data collected about the password--------------
    def classify(self):
        total = 0
        for x in range(0,6):
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
        #self.calulate_entropy()
        
        #print(self.password_vector)

#------------------What the program will use to classify the user password------------------
    def user_classify(self,password):
        self.get_weights(password)#get feature vector
        x = self.classify()#classify based on feature vector
        if x > 0:
            return True #Yes strong
        else:
            return False #No weak
#-------------------------------------------------------------------------------------------

                
#-----------When the predictions isn't correct-----------------------------
    def update_weights(self,actual_value):#if the classification is wrong then update the weights
        for x in range(0,6):
         #   print((self.learning * int(actual_value) * int(self.password_vector[x])))
            self.feature_vectors[x] = self.feature_vectors[x] + (self.learning * actual_value * self.password_vector[x])
        #print(self.password_vector)
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
        
        square = math.pow(total,self.password_vector[0])#amount of unique characters to the power of the length of the password
        entropy = math.log2(square) #log 2 of the total characters present
        self.password_vector[5] = entropy#set the entropy into the password vector
#----------------------------------------------------------------------