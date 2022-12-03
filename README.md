# Password Analyzer / Tracker

## Motivation:
  The motiviation behind this project comes from people using weak passwords along with reusing passwords. Which is the problem, if a weak password is used it would take no time for a program to obtain the password using brute force. If a password is reused then if one account gets compromised the other has a higher chance of being compromised than before. This program's goal is to help with both problems. To solve the first problem the program will classify passwords given 
using machine learning. To solve the second problem the program will keep track of past passwords if an account is made to ensure no password is reused.

## Program:
  The program will take a user password and with the help of machine learning (Perceptron) categorizes the given password as strong or weak. If the password is weak the program will give 10 new passwords based on the one given to improve the password and move it into the strong category. If a user account is made it will hash (sha256) the password chosen and say if this is a unique password for the user. If the password is found to not be unique the program will tell the user to come up with a different password to use. The user account will also be hashed to others can't see what hashes are linked to accounts.
  
## Program starts:
    1. Test Password
    2. Create Account
    3. Login
    4. Logout
    5. Exit
    
    Input: 
  
## Output: 
  Strong Password: This is a strong password<br>
  Weak Password: This is a weak password<br>
      -If logged in the program will given suggestions about passwords to use instead of the one provided based on the password inputted.

   
## Perceptron:
  The perceptron vectors will already be trained offline so the training wont need to take place with every startup of the program. Another key element of Perceptron is it won't learn after the training, it will go off the vector it has from the training data to classify passwords that are given. The feature vector of Percetron is the following in this order *length of password, number of special characters, number of digits, number of capital letters,  number of different characters (uppercase,  lowercase,  digits, special characters)*<br>
  
**Example**:<br>
Password: "Washb0rd123$#"<br>
Vector: [13,2,4,1,4]<br>


## Password Suggestions:
  The program will create 9 new passwords based on the one given. Next it will run the 9 new passwords through the machine learning vector and hopefully produce 9 passwords for the user to choose from. Then the user will then choose a password to use instead of the one they wanted to use.
