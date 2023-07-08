#Leetcode
#User function Template for python3
#Love babbar DSA Sheet Question 38 
from ast import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)