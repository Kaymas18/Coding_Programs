#GFG
#User function Template for python3
#Love babbar DSA Sheet Question 94 
class Solution:
    def middle(self,A,B,C):
        #code here
        if (A>B and A<C) or (A>C and A<B):
            return A
        elif (B>A and B<C) or (B>C and A>B):
            return B
        else:
            return C



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split())
        ob=Solution()
        print(ob.middle(A,B,C))
# } Driver Code Ends
