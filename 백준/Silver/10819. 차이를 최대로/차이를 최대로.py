from itertools import permutations

N=int(input())
A=list(map(int, input().split()))

a_combi=list(permutations(A, N))

lagrest_differ=0
for a in a_combi:
    total_differ=0
    for i in range(N):
        if i==N-1:
            break
        else:
            differ=abs(a[i]-a[i+1])
            total_differ+=differ
    if lagrest_differ<=total_differ:
        lagrest_differ=total_differ

print(lagrest_differ)