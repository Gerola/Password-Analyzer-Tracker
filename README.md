# Password Analyzer / Tracker

## Motivation:
[Insert Text]

## Program:
  The program will take a user password and with the help of machine learning (Perceptron) categorizes the given password as strong or weak. If the password is weak the program will give 10 new passwords based on the one given to improve the password and move it into the strong category. If a user account is made it will hash (sha256) the password chosen and say if this is a unique password for the user. If the password is found to not be unique the program will tell the user to come up with a different password to use. The user account will also be hashed to others can't see what hashes are linked to accounts.
  
## Program starts:
    Enter Password
    Login
    Create Account
    Exit
  
## Output: 
  "Insert phrase used". "Insert phrase used for not a strong password"

   
## Perceptron:
  The perceptron vectors will already be trained offline so the training wont need to take place with every startup of the program. Another key element of Perceptron is it wont learn after the training, it will go off the vector it has from the training data to classify passwords that are given. The feature vector of Percetron in this order *length of password, number of special characters, number of digits, number of capital letters,  number of different characters (uppercase,  lowercase,  digits, special characters),  entropy of the password*<br>
  
**Example**:<br>
Password: "Washb0rd123$#"<br>
Vector: [13,2,4,1,4,?]<br>


## Password Suggestions:
  The program will suggest 10 new passwords to use instead of the password provided given the password was classified as weak. The one chosen will then if an account has been created be hashed and written to the user's file so they will know this password has been used before and not to use it in the future.
