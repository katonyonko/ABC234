import io
import sys

_INPUT = """\
6
3
0 0
0 1
1 1
5
315 271
-2 -621
-205 -511
-952 482
165 463
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def dist(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**.5
  N=int(input())
  points=[list(map(int,input().split())) for _ in range(N)]
  ans=0
  for i in range(N):
    for j in range(N):
      ans=max(ans, dist(points[i],points[j]))
  print(ans)