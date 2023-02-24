#GFG
#User function Template for python3
#Love babbar DSA Sheet Question 9 of array

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        an = arr[n-1] - arr[0]
        x = arr[0] + k
        y = arr[n-1] - k
        for i in range(n-1):
            minel = min(x, arr[i+1] - k)
            maxel = max(y, arr[i] + k)
            if minel < 0:
                continue
            an = min(an, maxel-minel)

        return an


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends