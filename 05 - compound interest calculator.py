# compound interest calculator

print ("\n This is a Compound Interest Calculator \n")

#taking the inputs
initial = float(input("What is the initial amount : "))
years = float(input("For how much years you want to calculate : "))
interest = float(input("What is the annual interest rate : "))

#calculating the compound interest
# using the pow function to do exponential calculations
total =  (initial * (pow((1 + interest / 100), years)))

#calculating the interest amount
total_interest = (total - initial)

# using '%.2f' % to limiting the float value to 2 decimals
i_total = '%.2f' % total
i_interest = '%.2f' % total_interest

#printing the results
print ("\n Total Amount after " + str(years) + " years will be " + i_total)
print ("\n Total Interest after " + str(years) + " years will be " + i_interest + "\n")

# created by Abhishek
