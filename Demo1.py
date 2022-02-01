#Exercise 2.1 : Value of a coin
value_coin = int(input("Enter the value of a coin. "))
if value_coin == 1:
    print("That's a penny")
elif value_coin == 5:
    print("That's a Nickle")
elif value_coin == 10:
    print("That's a Dime")
elif value_coin == 25:
    print("That's a Quarter")
elif value_coin == 50:
    print("That's a Half Dollar")
else:
    print("That's not a valid coin!")
    
#Exercise 2.2 : To check the user has entered number between 1 to 10 and then check for even, odd and prime.
number = int(input("Enter the number between 1 and 10. "))

if number < 1 or number > 10:
    print("Error!! You should have entered a number between 1 and 10.")
if number <= 10 and number >= 1:
    if number % 2 == 0:
        print("You have entered even number.")
    else:
        print("You have entered odd number.")
    if number == 2 or number == 3 or number == 5 or number == 7:
        print("It is prime number.")
    else:
        print("The number is not prime.")

#Exercise 2.3 : To ask the user price of an item and eligibility of discounts.

price = int(input("Enter the price of the item. "))
while price <= 0:
    print("Please enter a positive number. You cannot enter zero or negative values.")
    price = int(input("Enter the price of the item. "))
if price > 0:
        if price <= 10:
            print("No discount")
        elif price > 10 and price < 50:
            print("10% discount")
        elif price > 50:
            print("20% discount")

#Exercise 2.4: To enter a starting number(integer), ending number(integer) and the word "even" or "odd"

start_num = int(input("Enter a starting number. "))
end_num = int(input("Enter an ending number. "))
even_odd = input("even or odd. ")
print("Starting Number: ", start_num)
print("Ending number: ", end_num)
print("Even or Odd: ", even_odd)
i = start_num + 1
while i > start_num and i < end_num:
    print(i)
    i += 2

#Exercise 2.5 : To prompt user to enter number of products, number of prices and compute total cost of all products.
products = int(input("Enter a number of products. "))
i = 0
total = 0
while i < products:
    price = int(input("Enter price for product #" + str(i+1) + ": "))
    i = i + 1
    total += price
print("Total cost", total)



#Exercise 2.6 :  "Shopping Cart Program" that asks the user for a series of product prices.
item_price = int(input("Enter an item price. "))
i = int(1)
tax = 0.07
tax1 = tax
total = item_price + tax
print("Tax on this item is " + str(tax) + ";" + "total price: " + str(total))
yes_no = input("Enter another price? (yes or no) ")
while yes_no == 'yes':
    item_price = int(input("Enter an item price. "))
    i += 1
    tax1 = tax * i
    tax1 = format(tax1, ".2f")
    total = item_price + float(tax1)
    print("Tax on this item is " + str(tax1) + ";" + "total price : " + str(total))
    yes_no = input("Enter another price? (yes or no)")
    
#Exercise 2.7 : To keep track of the total amount spent in addition to total tax value.   
item_price = int(input("Enter an item price. "))
i = int(1)
tax = 0.07
tax1 = tax
tax2 = tax
total = item_price + tax
total_sum = total
print("Tax on this item is " + str(tax) + ";" + "total price: " + str(total))
yes_no = input("Enter another price? (yes or no) ")
while yes_no == 'yes':
    item_price = int(input("Enter an item price. "))
    i += 1
    tax1 = tax * i
    tax1 = format(tax1, ".2f")
    total = item_price + float(tax1)
    total_sum = total + total_sum
    tax2 = float(tax1) + tax2
    print("Tax on this item is " + str(tax1) + ";" + "total price : " + str(total))
    yes_no = input("Enter another price? (yes or no) ")

print("Total amount due: " + str(total_sum))
tax2 = format(tax2, ".2f")
print("Total tax due: " + str(tax2))

#Exercise 2.8

answer = int(input("What is 2 + 2? "))
if answer == 4:
    print("Correct!")
while answer != 4:
    print("Wrong, try again.")
    answer = int(input("What is 2 + 2? "))
    if answer == 4:
        print("Correct!")
        
        
#Exercise 2.9

import random
num1 = random.randint(0,10)
num2 = random.randint(0,20)
answer = int(input("What is " + str(num1) + " + " + str(num2) + " equal? "))
num_sum = num1 + num2

if (answer == num_sum):
    print("Correct!")

while num_sum != answer:
    print("Incorrect, please try again")
    answer = int(input("What is " + str(num1) + " + " + str(num2) + " equal? "))
    if (answer == num_sum):
        print("Correct!")

    

    
    

    








    
    

    


