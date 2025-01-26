N = int(input())
M = int(input())

adj =[[] for _ in range(N)] # 인접 리스트 [[], [], ... []]

for _ in range(M):
    a, b= list(map(int, input().split()))
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

friends=adj[0]
invites=[]
for f in friends:
    invites.extend(adj[f])
invites.extend(friends)

if len(invites)==0:
    print(0)
else:
    print(len(set(invites))-1)