#Interview bit
class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        alph = "abcdefghijklmnopqrstuvwxyz"
        q = "".join(A)
        q = set(q)
        q = "".join(sorted(q))
        if q == alph:
            return 1
        else:
            return 0
