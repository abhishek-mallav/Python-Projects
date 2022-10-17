# simple interest calculator

print ("\n This is a Simple Interest Calculator \n")

#taking the inputs
initial = float(input("What is the initial amount : "))
years = float(input("For how much years you want to calculate : "))
interest = float(input("What is the annual interest rate : "))

#calculating the simple interest by implementing the mathematical formula
total_interest =  initial * years * interest / 100
#calculating the final total amount
total_amount = (total_interest + initial)

# using '%.2f' % to limiting the float value to 2 decimals
i_total = '%.2f' % total_amount
i_interest = '%.2f' % total_interest

#printing the results
print ("\n Total Amount after " + str(years) + " years will be " + i_total)
print ("\n Total Interest after " + str(years) + " years will be " + i_interest + "\n")