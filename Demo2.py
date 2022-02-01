#Assignment_HW3

#Exercise 1 : To count the number of A's, B's,C's, D's and F's

grades = [90,100,70,45,76,84,93,21,36,99,100]
result = []
output = 0
for i in range(len(grades)):
    if grades[i] >= 90:
        result.append("A")
    elif grades[i] >= 80:
        result.append("B")
    elif grades[i] >= 70:
        result.append("C")
    elif grades[i] >= 60:
        result.append("D")
    else:
        result.append("F")
print(result)
print("Count of A", result.count("A"))
print("Count of B", result.count("B"))
print("Count of C", result.count("C"))
print("Count of D", result.count("D"))
print("Count of F", result.count("F"))

#Exercise 2 : To apply a "class curve" to each score

grades = [93, 74, 66, 98, 34, 75, 79, 83, 84, 91, 12, 69, 72]
print("Before", grades)
after_grades = []
for score in grades:
    if score >= 90:
        after_grades.append(score)
    elif score >= 80 and score < 90:
        after_grades.append(score + 2)
    elif score >= 70 and score < 80:
        after_grades.append(score + 5)
    else:
        after_grades.append(score + 8)

print("After", after_grades)


#Exercise 3: Sales of a week

Sales_week = []
for i in range(7):
    i = i + 1
    sales = int(input("Enter sales for day #" + str(i) + ": "))
    Sales_week.append(sales)
print("Sales for the week : ", Sales_week)


#Exercise 4: To extract items of one list into another list

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
new_list1 = my_list[0:3]
print(new_list1)
new_list2 = my_list[1:4]
print(new_list2)
new_list3 = my_list[-4:]
print(new_list3)


#Exercise 5:  To check whether product exists in inventory or not
name = input("Enter the name of the product. ").lower()
products = ["apple", "pear", "peach", "banana"]
if name in products:
    print("The product name exists in our inventory")
else:
    print("Product not found!!")

#Exercise 6: To find all elements that exists in both the lists.
a = [1,2,3,4,5]
b = [2,3,10,11,12,1]
list3 = []
for x in a:
    for y in b:
        if x == y:
            list3.append(x)
print(list3)

#Exercise 7: To prompt the user to enter names and store in a list.
name = input("Enter the name. ")
namelist = []
while name != "end":
    if name not in namelist:
        namelist.append(name)
    name = input("Enter the name or type end to stop. ")
print(namelist)

#Exercise 8: To check whether product name is included in inventory list

products = ["apple", "pear", "peach", "banana"]
name = 0

while name != "end" and len(products) != 0:
    name = input("Enter the name of the product or type end to stop. ").lower()
    if name in products:
        i = products.index(name)
        del products[i]
        print(products)
    elif name != "end":
        print("The product is not present in the inventory.")

#Exercise 9: Lookup Table

products = ["peanut butter", "jelly", "bread"]
prices = [3.99, 2.99, 1.99]
name = input("Enter the product: ").lower()
i = products.index(name)
price1 = prices[i]
print("This product costs", price1)

#Exercise 10: To find the average of assignments scored by students
stud = int(input("How many students in the class? "))
assign = int(input("How many assignments in the class? "))
for i in range(stud):
    i = i+1
    total = 0
    avg = 0
    print("Student #" + str(i) + ": ")
    for j in range(assign):
        j = j+1
        marks = int(input("Assignment #" + str(j) + ": "))
        total += marks
    avg = total/assign
    print("Student #" + str(i) + " earned a " + str(avg))

























