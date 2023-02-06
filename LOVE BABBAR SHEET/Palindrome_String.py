#GFG
#User function Template for python3
#Love babbar DSA Sheet Question 48 of array
class Solution:
	def isPalindrome(self, S):
            # code here
            str=""
            i=0
            for i in S:
                str = i + str
            if str==S:
                return 1
            else:
                return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends