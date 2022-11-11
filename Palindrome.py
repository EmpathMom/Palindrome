## Went over  Strong  Number programs and fixed Strong Number programs
# Author :  Gaylene
# Created by : Gaylene
# Architect(s): Gaylene
# Developer(s): Gaylene
# Created Date: 11/10/22
# Description : Edit to Fibonacci with class
# Version: 2.0
# Modified by:Gaylene
# Modified Date: 11/10/2022
# Description: Write Palindrome program
#
##Write program  for Palindrome number.

#Example: 151
#get 151 % 10 = 1 rem 1
#remove right digit 151//10 = 15
#get 15 % 10 = 5 rem 5 
#remove right most digit 15//10 = 1
#get 1 % 10 = 1
#remove right most digit 1//10 = 0

n = int(input("Enter here if you dare: "))

given_number = n
generated_number = 0
while given_number > 0:
    #get rightmost digit for the iteration
    digit = given_number % 10
    #remove rightmost digit for each iteration
    given_number //= 10
    generated_number = generated_number * 10 + digit
if generated_number == n:
    print("You guessed right! your number is a Palindrome")
else:
    print("Sorry, Try again maybe you need to guess again")

##### REVISED #####

n = int(input("Enter here if you dare: "))

given_number = n
r = 0
while given_number > 0:
    #get rightmost digit for the iteration
    digit = given_number % 10
    #remove rightmost digit for each iteration
    given_number //= 10
    r = r * 10 + digit

if r == n:
    print("You guessed right! your number is a Palindrome")
else:
    print("Sorry, Try again maybe you need to guess again")
    
