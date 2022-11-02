# Password Analyzer / Tracker

## Motivation:
  The motiviation behind this project comes from people using weak passwords along with reusing passwords. Which is the problem, if a weak password is used it would take no time for a program to obtain the password using brute force. If a password is reused then if one account gets compromised the other has a higher chance of being compromised than before. This program's goal is to help with both problems. To solve the first problem the program will classify passwords given 
using machine learning. To solve the second problem the program will keep track of past passwords if an account is made to ensure no password is reused.

## Program:
  The program will take a user password and with the help of machine learning (Perceptron) categorizes the given password as strong or weak. If the password is weak the program will give 10 new passwords based on the one given to improve the password and move it into the strong category. If a user account is made it will hash (sha256) the password chosen and say if this is a unique password for the user. If the password is found to not be unique the program will tell the user to come up with a different password to use. The user account will also be hashed to others can't see what hashes are linked to accounts.
  
## Program starts:
    Test Password
    Find Account
    Create Account
    Login
    Logout
    Exit
  
## Output: 
  "Insert phrase used". "Insert phrase used for not a strong password"

   
## Perceptron:
  The perceptron vectors will already be trained offline so the training wont need to take place with every startup of the program. Another key element of Perceptron is it wont learn after the training, it will go off the vector it has from the training data to classify passwords that are given. The feature vector of Percetron in this order *length of password, number of special characters, number of digits, number of capital letters,  number of different characters (uppercase,  lowercase,  digits, special characters)*<br>
  
**Example**:<br>
Password: "Washb0rd123$#"<br>
Vector: [13,2,4,1,4]<br>


## Password Suggestions:
  The program will create 10 new passwords based on the one given. Next it will run the 10 new passwords through the machine learning vector and hopefully produce 10 passwords for the user to choose from. From the passwords displayed the user will then choose one to use.
