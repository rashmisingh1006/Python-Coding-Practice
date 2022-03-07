# Intro to Python 6850 - Homework #6

# Exercise #1:
try:
    myvar = open("most_popular_words_in_english.txt", "r")
    contents = myvar.read().splitlines()
    myvar.close()
    word = input("Enter a word in English. ").lower()
    if word in contents:
        print("The given word is present.")
    else:
        print("The given word is not present.")
except:
    print("Something went wrong!!")


# Exercise  # 2: (6 points) Security Program to enter the username and password.

username = input("Enter the username. ")
password = input("Enter the password. ")
with open("security.txt", mode='w') as my_file:
    text = my_file.write(username + "\n" + password)

# Exercise #3:

try:
    with open("security.txt", mode='r') as my_file:
        contents = my_file.read()
        print(contents)
        line = contents.strip().split("\n")
        username = line[0]
        password = line[1]
        user = input("Enter the username: ")
        pwd = input("Enter your password: ")
    if (user == username) and (pwd == password):
        print("Congratulations!! You have logged in successfully.")
    else:
        print("Username/Password entered are incorrect!")

except Exception as ex:
    print(f"error!!{ex}")

# Exercise 4 : Write a program that opens up a file named "testscores.txt".
# This file contains the following information in the following format:

myfile = open('testscores.txt', 'r')
contents = myfile.read().splitlines()
print(contents)
myfile.close()
name = contents[0]

def average(contents):
    sum = 0
    num = 3
    for i in range(1,len(contents)):
        sum = sum + int(contents[i])
    average = sum/num
    print("The average score for the " + name + "is " + str(average))

average(contents)





