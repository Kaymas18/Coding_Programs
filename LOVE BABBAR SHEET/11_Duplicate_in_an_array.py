#Leetcode
#User function Template for python3
#Love babbar DSA Sheet Question 11 of array
def dup(arr,n):
    arr.sort()
    i=0
    while(i<n):
        if arr[i]==arr[i+1]:
            x=arr[i]
            break
        i=i+1
    return x
n=int(input())
arr=list(map(int,input().strip().split()))
print(dup(arr,n))