#GFG
#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
            y=[]
            # code here
            y=[*set(arr)]
            l=len(y)
            y.sort()
            y.reverse()
            if l==1:
                return -1
            else:
                return y[1]
		

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends