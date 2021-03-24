
# 1.
fname = input("What's your first name?")
lname = input("What's your last name?")
age = input("How old are you?")

print(f"My name is {fname} {lname} and I am {age} years old.")

# 2. 
one = str(1)
two = str(2)
three = str(3)
print(one, two, three)

print(type(one))

# 3.
ftemp = int(input("What's the current temp. in F? "))
ctemp = (ftemp - 32) * 5.0
ctemp = ctemp / 9.0
print(f"The temperature in degrees C is {ctemp}")

# 4a.
# Hint: You can solve this problem without a forloop, but if you can figure it out using a for loop try to do it that way
# Write a program that asks the user to input how much money they have saved up. 
# Then ask the user to input a monthly growth rate (%) example: 5% would mean their savings would increase by 5% monthly. 
# Calculate how much the user would have at the end of each month for 12 months & print it all to the user
# Example: 
# savings = 100
# growth_rate = 5%

# End of Januaray = $105
# End of February = 110.25
# End of March = $115.76...
# End of Decemeber...

savings = int(input("enter your savings, in $: "))
gr = int(input("enter in a monthly growth rate, in %: ")) #gr = growth rate
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for x in months:
    # x += 1
    # gr = gr/100 #makes gr a percent
    # newmon = int(savings * gr) #extra money from increase
    # totalsavings = int(savings + newmon)
    # savings = totalsavings
    # print(f"your savings for month {x} are {totalsavings} dollars")
    total = savings + ((gr)/100) * savings
    savings = total
    print(f"Your savings for month {x} are ${total}")
    

    
    
    
    
   