
# 1.
# Create Input Variables for your first name, last name and age.
fname = input("What's your first name?")
lname = input("What's your last name?")
age = input("How old are you?")
# Then print out your full name and age within a sentence -> My name is Hunter Macias & 
# I am 20 years old
print(f"My name is {fname} {lname} and I am {age} years old.")

# 2. 
# create 3 different variables with any whole number assined as the value and convert them into a string using the str() constructor.
# once you convert them print out the variables. Example: convert 3 to '3'
one = str(1)
two = str(2)
three = str(3)
print(one, two, three)
# if you use print(type(<var_name>)) this will print out the type of variable for example x = 3 would print 'int' and x = '3' would print 'str'
print(type(one))

# 3.
# Write a program that asks the user for the current temperature (F) and then use their Input calculate temperature in (C). 
# Here is the formula to conver F to C => C = (Fahrenheit - 32) * 5.0/9.0
# Once you calculate Celcius print out the conversion to the user
ftemp = int(input("What's the current temp. in F? "))
ctemp = (ftemp - 32) * 5.0
ctemp = ctemp / 9.0
print(ctemp)
