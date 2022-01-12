import io
import sys

_INPUT = """\
6
152
88
8989898989
101
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def f(x):
    res=0
    for i in range(len(x)):
      res += x[len(x)-i-1]*10**i
    return res
  X=list(input())
  N=len(X)
  X=[int(X[i]) for i in range(N)]
  ans=10**100
  for i in range(10):
    kouho=[X[0]-i*j for j in range(N)]
    if kouho[-1]>=0 and f(kouho)>=f(X):
      ans=min(ans,f(kouho)) 
  for i in range(10):
    kouho=[X[0]+i*j for j in range(N)]
    if kouho[-1]<10 and f(kouho)>=f(X):
      ans=min(ans,f(kouho)) 
  if X[0]==9:
    for i in range(10):
      kouho=[1-i*j for j in range(N)]
      if kouho[-1]>=0 and f(kouho)>=f(X):
        ans=min(ans,f(kouho)) 
    for i in range(10):
      kouho=[1+i*j for j in range(N+1)]
      if kouho[-1]<10 and f(kouho)>=f(X):
        ans=min(ans,f(kouho)) 
  else:
    for i in range(10):
      kouho=[X[0]+1-i*j for j in range(N)]
      if kouho[-1]>=0 and f(kouho)>=f(X):
        ans=min(ans,f(kouho)) 
    for i in range(10):
      kouho=[X[0]+1+i*j for j in range(N+1)]
      if kouho[-1]<10 and f(kouho)>=f(X):
        ans=min(ans,f(kouho)) 
  print(ans)