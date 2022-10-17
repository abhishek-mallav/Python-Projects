# guess the random number game v2.0

# importing the random python library for random number generation
import random

# putting n as a variavle for the random number
# using tht randint function to limit numbers to 1-100
n=int((random.randint(0,100)))

# putting c as a variable for number of chances
c = 7
print (c)

# \n is used to jump to next line like enter in notepad
# printing c as str(c) because in python strings with strings can be printed and integers with integers no mis match
# the str function converts the integer or float value to string
print ("\nGuess the correct Random Number \n \nyou have " + str(c) + " total chances \n \nThe Random Number is in between 1-100\n")


# using a while loop to loop the code for number of chances
# also while the code is looping nesting the game logic code inside it
while c > 0:
              x = int(input("input a number\n > "))
              if x>n:
                            # if the input number is more than the random number
                            print("the number is less than " + str(x) + "\n")
                            print("you have " + str(c-1) + " chances left")
              if x<n:
                            # if the input number is less than the random number
                            print("the number is more than " + str(x) + "\n")
                            print("you have " + str(c-1) + " chances left")
              if x==n:
                            # if the input number is equal to the random number
                            print("Congrulations You Guessed the Right Number")
                            c = 0
              elif c <= 1 :
                            # if the input number is not equal to the random number and all chances are over
                            print("you lost the game. \n \nThe Number was " + str(n) + "\n")
                            exit()
              c = c - 1

