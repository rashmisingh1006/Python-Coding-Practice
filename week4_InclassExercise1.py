#4.1. Split Number List
String1 = '10 67 123 46 20 18 36 250'
number_list = String1.split()
print(number_list)
String2 = '10,67,123,46,20,18,36,250'
number_list2 = String2.split(",")
print(number_list2)

#4.2 Split Data into List

str = '90,67,87,102,77,80'
list2 = str.split(",")
print(list2)
total = 0
for i in list2:
    total += int(i)
print(total)

#alternative

scores1 = '90,67,87,102,77,80'
int_score_list = [int(x) for x in scores1.split(",")]
output = sum(int_score_list)
print(output)

#4.3 Slice Lists

a = [1,2,3,4,5,6,7,8,9]
sliced = a[:4]
print(sliced)

#4.4 Slice Lists with Increment
my_list = ['a','b','c','d','e','f','g']
output = my_list[::2]
print(output)