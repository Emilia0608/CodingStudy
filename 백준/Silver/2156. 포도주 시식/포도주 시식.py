N= int(input())
wine=[]
for _ in range(N):
    wine.append(int(input()))

dp=[0] * N
dp[0] = wine[0]
if N > 1:
    dp[1] = wine[0] + wine[1]

for i in range(2, N):
    non_drink=dp[i-1]
    only_drink=dp[i-2]+wine[i]
    if i>=3:
        both_drink=dp[i-3]+wine[i-1]+wine[i]
    else:
        both_drink=wine[i-1]+wine[i]
    dp[i]=max(non_drink, only_drink, both_drink)
print(max(dp))