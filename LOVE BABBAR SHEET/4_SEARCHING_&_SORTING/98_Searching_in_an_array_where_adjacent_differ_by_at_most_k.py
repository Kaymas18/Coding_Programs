#GFG
#User function Template for python3
#Love babbar DSA Sheet Question 98 of array


def search (arr, n, x, k) : 
    #Complete the function
    i,c=0,0
    while i<len(arr):
        if arr[i]==x:
            c=i
            return c
        i=i+1
    return -1
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    n, k = map(int , input().split())
    arr = list(map(int, input().strip().split()))
    x = int(input())
    ans = search(arr, n, x, k)
    print(ans)




# } Driver Code Ends