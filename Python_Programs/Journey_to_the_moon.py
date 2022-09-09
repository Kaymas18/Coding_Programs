import sys

def findPrt(a):
  if prt[a] < 0:
    return a
  prt[a] = findPrt(prt[a])
  return prt[a]

def join(a, b):
  a = findPrt(a)
  b = findPrt(b)
  if a != b:
    prt[a] = b

n, i = sys.stdin.readline().split()
n, i = int(n), int(i)
prt = [-1 for k in range(n)]
for k in range(i):
  a, b = sys.stdin.readline().split()
  a, b = int(a), int(b)
  join(a, b)

count = [0 for k in range(n)]
for k in range(n):
  pk = findPrt(k)
  count[pk] = count[pk] + 1
print(sum([a * (n - a) for a in count]) // 2)

