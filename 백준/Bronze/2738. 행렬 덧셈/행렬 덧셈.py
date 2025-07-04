N, M= map(int, input().split(" "))
sum=[]

for _ in range(N):
    sum.append(list(map(int, input().split(" "))))

for i in range(N):
    b_row=list(map(int, input().split(" ")))
    sum[i]=[x+y for x,y in zip(sum[i], b_row)]

for su in sum:
    print(" ".join(map(str, su)))