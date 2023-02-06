#GFG
#User function Template for python3
#Love babbar DSA Sheet Question 30 of array
class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        i=0
        md=A[N-1]
        while(i+M-1<N):
            c=A[i+M-1]-A[i]
            if c<md:
                md=c
            i=i+1
        return md
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends