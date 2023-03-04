#LeetCode
#User function Template for python3
#Love babbar DSA Sheet Question 92 of array
from ast import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,k=0,0
        while i<len(nums):
            if target==nums[i]:
                k=i
                return k
            i=i+1
        return -1