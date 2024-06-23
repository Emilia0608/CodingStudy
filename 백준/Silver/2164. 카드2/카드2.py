from collections import deque

d=deque([])

n=int(input())
for i in range(1, n+1):
  d.append(i)

while len(d)>1:
  d.popleft()
  move_card=d.popleft()
  d.append(move_card)
  
if len(d)==1:
  print(d[0])