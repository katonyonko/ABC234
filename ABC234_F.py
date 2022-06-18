import io
import sys

_INPUT = """\
6
aab
aaa
abcdefghijklmnopqrstuvwxyz
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  S=input()
  C=[0]*26
  F=[1]
  N=len(S)
  for i in range(N):
      F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(N):
      I.append(I[-1]*(N-i)%mod)
  I=I[::-1]
  for i in range(N):
    C[ord(S[i])-ord('a')]+=1
  dp=[[0]*(N+1) for _ in range(27)]
  dp[0][0]=1
  for i in range(26):
    for j in range(N+1):
      for k in range(C[i]+1):
        if j>=k: dp[i+1][j]=(dp[i+1][j]+dp[i][j-k]*F[j]*I[k]*I[j-k])%mod
  print((sum(dp[-1])-1)%mod)