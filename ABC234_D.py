import io
import sys

_INPUT = """\
6
3 2
1 2 3
11 5
3 7 2 5 11 6 1 9 8 10 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappop, heappush
  N,K=map(int,input().split())
  P=list(map(int,input().split()))
  h=[]
  for i in range(K):
    heappush(h,P[i])
  for i in range(N-K+1):
    x=heappop(h)
    print(x)
    if i<N-K:
      heappush(h, max(x,P[i+K]))