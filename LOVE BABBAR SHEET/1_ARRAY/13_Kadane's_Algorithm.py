#GFG
#User function Template for python3
#Love babbar DSA Sheet Question 13 of array
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        maxi = arr[0]
        Sum1 = 0
        for i in range(0, N):
            Sum1 += arr[i]
            maxi = max([maxi, Sum1])
            if Sum1 < 0:
                Sum1 = 0;
            
        return maxi
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends