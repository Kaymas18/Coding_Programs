# Binary Search in python


def binarySearch(array, x, low, high):

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1


n=int(input())
array=list(map(int,input().strip().split()))
x = int(input())

result = binarySearch(array, x, 0, n-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")