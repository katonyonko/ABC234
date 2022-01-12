import io
import sys

_INPUT = """\
6
0
3
10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  t=int(input())
  def f(x):
    return x**2+2*x+3
  print(f(f(f(t)+t)+f(f(t))))