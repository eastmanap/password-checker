# Apollos Eastman
# Dec 13 2024
# Text adventure

import time
password = input('Type your password:')
alphabet =  'abcdefghijklmnopqrstuvwxyz'
special_char = '~`! @#$%^&*()_-+={[}]|\:;"\'<,>.?/'
nums = '1234567890'
score = 0

#Check for lowercase  
time.sleep(3)
lowercase = False

for character in password:
    if character in alphabet:  
        lowercase = True
    
    if lowercase:
        print('Your password contains lowercase characters.')
        score = score + 5
        print('+5 points!\n')
        break

if not lowercase:
    print('Your password DOES NOT contain lowercase characters.\n')

#Check for uppercase
time.sleep(3)
uppercase = False

for character in password:
    if character in alphabet.upper():  
        uppercase = True
    
    if uppercase:
        print('Your password contains uppercase characters.')
        score = score + 5
        print('+5 points!\n')
        break

if not uppercase:
    print('Your password DOES NOT contain uppercase characters.\n')

#Check for special characters
time.sleep(3)
is_special = False

for character in password:
    if character in special_char:  
        is_special = True
    
    if is_special:
        print('Your password contains at least one special character.')
        score = score + 5
        print('+5 points!\n')
        break

if not is_special:
    print('Your password DOES NOT contain at least one special character.\n')

#Check for numbers
time.sleep(3)
is_nums = False

for character in password:
    if character in nums:  
        is_nums = True
    
    if is_nums:
        print('Your password contains numbers.')
        score = score + 5
        print('+5 points!\n')
        break

if not is_nums:
    print('Your password DOES NOT contain numbers.\n')

#Check for length
time.sleep(3)
is_len = False

if len(password) >= 8: 
    is_len = True
    
if is_len:
    print('Your password is at least 8 characters long.')
    score = score + 5
    print('+5 points!\n')

if not is_len:
    print('Your password IS NOT at least 8 characters long.\n')

# final score
time.sleep(3)

if score == 25:
  print(f'Great job! You met all the requirements with a final score of {score}!')
elif score > 14:
  print(f'Great job! You met most of the requirements with a final score of {score}!')
elif score < 11:
  print(f'Whoops! You met some of the requirements but only got a final score of {score}!')
elif score == 0:
    print(f'Oh no! You met none of the requirements and got a final score of {score}!')
else:
    print('Oops! Something went wrong, please try again!')
