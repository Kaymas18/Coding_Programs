#GFG
#User function Template for python3
#Love babbar DSA Sheet Question 90 of array
def find(arr,n,x):
    ind = []
    if x in arr:
        for i in range(n):
            if arr[i] == x:
                ind.append(i)
        return ind[0],ind[-1]
    else:
        return -1,-1


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends