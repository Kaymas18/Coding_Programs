#GFG
#User function Template for python3
#Love babbar DSA Sheet Question 96 of array
class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        total_sum=(n*(n+1)//2)
        su=sum(set(arr))
        s=sum(arr)
        y=s-su
        k=total_sum-su
        return((y,k))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends