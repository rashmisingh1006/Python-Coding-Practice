# To find the smallest number in an array
arr = [90,100,10]
def findSmallest(arr):
    smallest = arr[0]  #store the smallest value
    smallest_index = 0  #store the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

print(findSmallest(arr))

# Program to write selection sort
def selectionSort(arr):   #Sorts an array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)  #find the smallest element in the array and adds to the new array
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort(arr))


