from itertools import combinations

heights=[]
for _ in range(9):
    height=int(input())
    heights.append(height)

heights_combi=list(combinations(heights, 7))
for combi in heights_combi:
    if sum(combi)==100:
        target=combi
        break
target=list(target)
target.sort()
for t in target:
    print(t)