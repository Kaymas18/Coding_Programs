#GFG
#User function Template for python3
#Love babbar DSA Sheet Question 88 

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        if len(str1) != len(str2):
            return 0
        dic1,dic2 = {},{}
        for i , j in zip(str1 ,str2):
            if i not in dic1 and j not in dic2:
                dic1[i] = j
                dic2[j] = i
            elif i in dic1 and j in dic2 and dic1[i] != j and dic2[j]!=i:
                return 0
            elif i in dic1 and j not in dic2:
                return 0
            elif i not in dic1 and j in dic2:
                return 0
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends