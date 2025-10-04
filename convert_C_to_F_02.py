# FILE NAME - convert_C_to_F_02.py

# NAME: Norgie Caceres
# DATE: 10/03/2025
# BRIEF DESCRIPTION: This script will convert Celsius to Fahrenheit and vice versa based on user input.
# and will also output a menu for the user to choose from.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("==== Temperature Converter ====\n")



print(" 1. Convert from Celsius to Fahrenheit")

print(" 2. Convert from Fahrenheit to Celsius\n")



Choice = int(input("Please choose from the above menu: "))




Temperature = float(input("Enter a temperature to convert: "))


if Choice == 1:
    c_to_f = Temperature *9/5 + 32

    print(f"\n{Temperature} degrees Celsius is {c_to_f} degrees Farenheit.")
  
elif Choice == 2:
    f_to_c = (Temperature - 32) * 5/9
    print(f"\n{Temperature} degrees Farenheit is {f_to_c} degrees Celsius.")
else:
    print()

    






########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

I learened that it's possible to define variable withing an if statement, 
which can keep the code more organized and context-specific.




'''
