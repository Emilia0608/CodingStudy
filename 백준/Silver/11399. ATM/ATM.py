N= int(input())
P=list(map(int, input().split()))
P.sort()

total=0
for i in range(1, len(P)+1):
    tmp=sum(P[:i])
    total+=tmp

print(total)