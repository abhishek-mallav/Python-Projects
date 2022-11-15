# guess the ramdom number game

# importing the random python library for random number generation
import random

# making the random number a variable "n"
# using tht randint function to limit numbers to 1-100
n=int((random.randint(0,100)))

# \n is used to jump to next line like enter in notepad
print ("\nGuess the correct Random Number \nThe Random Number is in between 1-100\n")

# using if statements for game logic
print("You Have 7 Chances to Guess Correctly")
x = int(input("input a number \n > "))
if x>n:
    print("the number is less than " + str(x) + "\n")
if x<n:
    print("the number is more than " + str(x) + "\n")
if x==n:
    print("Congrulations You Guessed the Right Number")
    exit()

print("You Have 6 Chances Left")
x = int(input("input a number \n > "))
if x>n:
    print("the number is less than " + str(x) + "\n")
if x<n:
    print("the number is more than " + str(x) + "\n")
if x==n:
    print("Congrulations You Guessed the Right Number")
    exit()

print("You Have 5 Chances Left")
x = int(input("input a number \n > "))
if x>n:
    print("the number is less than " + str(x) + "\n")
if x<n:
    print("the number is more than " + str(x) + "\n")
if x==n:
    print("Congrulations You Guessed the Right Number")
    exit()

print("You Have 4 Chances Left")
x = int(input("input a number \n > "))
if x>n:
    print("the number is less than " + str(x) + "\n")
if x<n:
    print("the number is more than " + str(x) + "\n")
if x==n:
    print("Congrulations You Guessed the Right Number")
    exit()

print("You Have 3 Chances Left")
x = int(input("input a number \n > "))
if x>n:
    print("the number is less than " + str(x) + "\n")
if x<n:
    print("the number is more than " + str(x) + "\n")
if x==n:
    print("Congrulations You Guessed the Right Number")
    exit()

print("You Have 2 Chances Left")
x = int(input("input a number \n > "))
if x>n:
    print("the number is less than " + str(x) + "\n")
if x<n:
    print("the number is more than " + str(x) + "\n")
if x==n:
    print("Congrulations You Guessed the Right Number")
    exit()

print("You Have 1 Chances Left")
x = int(input("input a number \n > "))
if x>n:
    print("the number is less than " + str(x) + "\n")
if x<n:
    print("the number is more than " + str(x) + "\n")
if x==n:
    print("Congrulations You Guessed the Right Number")
    exit()

print("This is Your Last Chance")
x = int(input("input a number \n > "))
if x>n:
    print("You Lost The Game Try Again \nThe Number was " + str(n))
if x<n:
    print("You Lost The Game Try Again \nThe Number was " + str(n))
if x==n:
    print("Congrulations You Guessed the Right Number")
    exit()

# created by Abhishek
