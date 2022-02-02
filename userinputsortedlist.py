# Write a program to ask user to input a week sales for 7 days and then store the week sales in ascending order
# and print the sorted results to the user.

week_sales = []
for day in range(7):
    day = day + 1
    sales = int(input("Enter the sales for day" + str(day) + "#: "))
    week_sales.append(sales)
print(week_sales)

def findSmallest(week_sales):
    smallest = week_sales[0]  #store the smallest value
    smallest_index = 0  #store the index of the smallest value
    for i in range(1, len(week_sales)):
        if week_sales[i] < smallest:
            smallest = week_sales[i]
            smallest_index = i
    return smallest_index

print(findSmallest(week_sales))

# Program to write selection sort
def selectionSort(week_sales):   #Sorts an array
    newArr = []
    for i in range(len(week_sales)):
        smallest = findSmallest(week_sales)  #find the smallest element in the array and adds to the new array
        newArr.append(week_sales.pop(smallest)) # pop function takes in an index value, then check whether the item
                                                # exists in the list. if the item exists in the list, it will remove the item from the list.
    return newArr

print(selectionSort(week_sales))



