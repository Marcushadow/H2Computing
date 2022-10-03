sizeOfArray = input("Please enter size of array: ")
while((not sizeOfArray.isdigit()) or int(sizeOfArray)<5 or int(sizeOfArray) > 12):
    sizeOfArray = input("ERROR! Please enter size of array: ")

sizeOfArray = int(sizeOfArray)
arr = []

for i in range(sizeOfArray):
    arr.append(int(input("Please enter an integer: ")))


def quicksort(array, left, right):
    if (left < right):
        pivot = partition(array, left, right)
        quicksort(array, left, pivot - 1)
        quicksort(array, pivot + 1, right)
    
    
def partition(array, left, right):
    pivot = array[left]

    l = left + 1
    r = right
    while (l <= r):
        while(l <= r and array[l] <= pivot):
            l += 1
        
        while(l <= r and array[r] > pivot):
            r -= 1

        if(l <= r):
            array[r] , array[l] = array[l], array[r]
        
    array[r], array[left] = array[left], array[r]

    return r
        
quicksort(arr, 0, len(arr)-1)
print(arr)