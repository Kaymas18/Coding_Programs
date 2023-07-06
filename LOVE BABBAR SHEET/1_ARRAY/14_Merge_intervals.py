#Leetcode
#User function Template for python3
#Love babbar DSA Sheet Question 14 
from ast import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        x = sorted(intervals, key = lambda i: i[0])
        li = list()

        for start, end in x:
            if li and li[-1][1] >= start:
                li[-1][1] = max(li[-1][1], end)
            else:
                li.append([start, end])
            
        return li