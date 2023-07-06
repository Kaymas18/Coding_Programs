#GFG
#User function Template for python3
#Love babbar DSA Sheet Question 35 

class Solution:
	def find_median(self, v):
            # Code here
            l= len(v)
            a=sorted(v)
            if l%2==0:
                     med=(a[(l//2)-1] + a[l//2])//2           
            else:
                    med=(a[(l//2)])
            return med


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends