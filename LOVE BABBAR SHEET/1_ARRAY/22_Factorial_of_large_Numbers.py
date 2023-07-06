#GFG
#User function Template for python3
#Love babbar DSA Sheet Question 22 
class Solution:
    def factorial(self, N):
        #code here
        i=1
        for j in range(1,N+1,1):
            i*=j
        return str(i)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()
    
# } Driver Code Ends