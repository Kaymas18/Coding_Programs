#GFG
#User function Template for python3
#Love babbar DSA Sheet Question 36 

class Solution:
    def MedianOfArrays(self, array1, array2):
            ar=array1+array2
            ar.sort()
            l=len(ar)
            if(l%2==0):
                s=((ar[l//2]+ar[(l//2)-1])/2)
                if(s%1!=0):
                    pass
                else:
                    s=int(s)
            else:
                s=(ar[l//2])
            return s

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends