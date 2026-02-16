import string

password = "123456"

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case ,lower_case ,special ,digits]

length = len(password)

score = 0 

with open("portfolio/common.txt" ,'r') as f:
    common = f.read().splitlines()

if password in common:
    print("password is found in our database score: 0/7")
    exit()


if length > 8:
    score += 1 
if length > 12:
    score += 1 
if length > 17:
    score += 1 
if length > 20:
    score += 1 

print(f'password lenght : {str(length)} adding {str(score)} points ')

if sum(characters) > 1:
    score +=1
if sum(characters) > 2:
    score +=1
if sum(characters) > 3:
    score +=1

print(f"password has {str(sum(characters))} different char type , adding {str(sum(characters) - 1)} point")

if score < 4 :
    print(f"the password is quite weak {str(score)} /7")
elif score == 4 :
    print(f"the password is ok  {str(score)} /7")
elif score > 4 and score < 6:
    print(f"the password is pretty good {str(score)} /7")
elif score > 6 :
    print(f"the password is quite weak {str(score)} /7")

