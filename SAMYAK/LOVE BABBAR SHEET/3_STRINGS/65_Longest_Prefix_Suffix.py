#GFG
#User function Template for python3
#Love babbar DSA Sheet Question 65 

class Solution:
	def lps(self, s):
		# code here
            lp=[0]*len(s)
            prLPS,i=0,1
            while i < len(s):
                            if s[prLPS]==s[i]:
                                lp[i]=prLPS+1
                                prLPS+=1
                                i+=1
                            elif prLPS==0:
                                lp[i]=0
                                i+=1
                                
                            else:
                                prLPS = lp[prLPS-1]
                                    
            return lp[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.lps(s)
		print(answer)

# } Driver Code Ends