#Leetcode
#User function Template for python3
#Love babbar DSA Sheet Question 17 
from ast import List
class Solution:
   def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        maxi = 0
        mini = prices[0]
        for i in range(1, len(prices)):		
            maxi = max(maxi, prices[i] - mini)
            mini = min(mini, prices[i])
        return maxi
        