# Computer Security 327 Course Project

## Program:
  Take a user password and with the help of machine learning (Perceptron) categorizes the given password as strong or weak. If the password is weak the program will give a suggestion on how to improve the password to move it into the strong category. If a user account is made it will hash (sha256) the password chosen and say if this is a unique password for the user. If the password is found to not be unique the program will tell the user to come up with a different password to use. The user account will also be hashed to others can't see what hashes are linked to accounts.
  
  
## Input:
  Password from User under consideration.
  
## Output: 
  "Insert phrase used". "Insert phrase used for not a strong password"

   
## Perceptron:
  The perceptron vectors will already be trained offline so the training wont need to take place with every startup of the program. It wont learn after the training either.


## Password Suggestions:
  The program will suggest a new password if the one provided is weak.
