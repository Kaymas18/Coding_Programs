'''
GFG
User function Template for python3
Love babbar DSA Sheet Question 4 of array
'''


class Solution:
    def sort012(self, arr, n):
        # Count the occurrences of 0, 1, and 2
        count_0 = 0
        count_1 = 0
        count_2 = 0

        for num in arr:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            elif num == 2:
                count_2 += 1

        # Update the array with the sorted elements
        i = 0
        while count_0 > 0:
            arr[i] = 0
            i += 1
            count_0 -= 1

        while count_1 > 0:
            arr[i] = 1
            i += 1
            count_1 -= 1

        while count_2 > 0:
            arr[i] = 2
            i += 1
            count_2 -= 1


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sort012(arr, n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
