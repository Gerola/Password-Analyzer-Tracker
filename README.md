# Password Analyzer / Tracker

## Motivation:
  The motiviation behind this project comes from people using weak passwords along with reusing passwords. Which is the problem, if a weak password is used it would take no time for a program to obtain the password using brute force. If a password is reused then if one account gets compromised the other has a higher chance of being compromised than before. This program's goal is to help with both problems. To solve the first problem the program will classify passwords given 
using machine learning. To solve the second problem the program will keep track of past passwords if an account is made to ensure no password is reused.

## Program:
  The program will take a user password and with the help of machine learning (Perceptron) categorizes the given password as strong or weak. If the password is weak and the user is logged in the program will give hopefully 9 new passwords based on the one given to improve the password and move it into the strong category. If a user account is made and logged in, it will hash (sha512) the password chosen and say if this is a unique password for the user. If the password is found to not be unique the program will tell the user to come up with a different password to use. The user account will be hashed (sha512) so others can't see what passwords are linked to what accounts and a salt value will also be added before the name is hashed.  
  
## Perceptron:
  The perceptron vectors will already be trained offline so training won't need to take place everytime the program is run. Another key element is Perceptron won't learn after the training, it will go off the vector it has from the training data to classify passwords that are given. The feature vector of Percetron is the following in this order *if the password is longer than 20 characters, number of special characters, number of digits, number of capital letters,  number of different characters (uppercase,  lowercase,  digits, special characters)*<br>
  
**Example**:<br>
Password: "Washb0rd123$#"<br>
Vector: [0,2,4,1,4]<br>

## Password Suggestions:
  The program will create 9 new passwords based on the one given. Next it will run the 9 new passwords through the machine learning vector and hopefully produce 9 passwords for the user to choose from. Then the user will choose a password generated instead of the one they wanted.
