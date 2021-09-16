# Code written by Tanner McCarthy
# Date: 09/15/21 
# Intro to programming BCS FSC
# Professor Fried

#Take in user's name
userName = str(input("Please enter your name "))

#Take in the values for each variable 
userFutVal = int(input("Hello " + userName + ", please enter the future value: " ))
userIntRate = float(input("Please enter the interest rate: " ))
userTime = int(input("Please enter the time in years: " ))

#formula for finding the starting value
startingVal = float((userFutVal / ((1 + userIntRate)**userTime)))
startingVal = round(startingVal, 2)

print("This is what your starting value should be ", startingVal)

#\n inserts a blank line so that the formatting looks nice in the terminal/console

#we ask the user for the starting value
startVal = float(input("\nPlease enter the starting value: "))
#we ask for the interest rate
intRate = float(input("Please enter the interest rate: "))
#we ask for how long the money will grow
years  = float(input("please tell me how long you want the money to grow: "))

#we calculate the final value with the values the user gave us
finalVal = float( (startVal * ((1 + intRate)**years) ) )

#we round the final value to two deciaml places
finalVal = round(finalVal, 2)

#finally we print the final value for the user to see
print(finalVal)

