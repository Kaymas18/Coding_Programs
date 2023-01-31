#Interview bit
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        val1=A[0:2]
        val2=A[3:5]
        hour=int(val1)
        minu=int(val2)
        cnt=0
        while (hour//10!=minu%10) or (hour%10!=minu//10):
            cnt+=1
            minu+=1
            if minu==60:
                hour+=1
                minu=0
            if hour==24:
                hour=0  
        return cnt        