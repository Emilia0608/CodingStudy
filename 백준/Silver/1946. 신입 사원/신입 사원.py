import sys
T= int(input())
input=sys.stdin.readline

for _ in range(T):
  N= int(input())
  candidates = [] 

  for _ in range(N):
    s, m= map(int, input().split())
    candidates.append((s, m))
  
  # (s, m)
  candidates.sort()
  top_ranking= 1e9
  count=0

  for i in range(N):
    if candidates[i][1] < top_ranking:
      count+=1
      top_ranking= candidates[i][1]

  print(count)