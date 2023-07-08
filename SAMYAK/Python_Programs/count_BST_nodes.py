class Solution:
    def getCount(self,root,low,high):
        ##Your code here
        c = 0
        def aj(root,l,h,c):
            if not root:
                return 0
        
            left = aj(root.left,l,h,c)
            right = aj(root.right,l,h,c)
            if l <= root.data <= h:
                return 1 + left + right
            else:
                return right + left
        return aj(root,low,high,c) 

from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
 
def buildTree(s):

    if(len(s)==0 or s[0]=="N"):           
        return None

    ip=list(map(str,s.split()))

    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    q.append(root)                            
    size=size+1 

    i=1                                       
    while(size>0 and i<len(ip)):
 
        currNode=q[0]
        q.popleft()
        size=size-1
        
        currVal=ip[i]
        
        if(currVal!="N"):
            
            currNode.left=Node(int(currVal))
            
            q.append(currNode.left)
            size=size+1
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        if(currVal!="N"):
            
            currNode.right=Node(int(currVal))
            
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        l, r=map(int, input().split())
        obj=Solution()
        print(obj.getCount(root,l,r))

