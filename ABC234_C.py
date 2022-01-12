import io
import sys

_INPUT = """\
6
3
11
923423423420220108
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  K=int(input())
  ans=[str(0) if (K>>i)&1==0 else str(2) for i in range(60)]
  ans=ans[::-1]
  x=0
  for i in range(60):
    if ans[i]==str(0):
      x+=1
    else:
      break
  print(*ans[x:], sep='')