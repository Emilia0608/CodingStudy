N=int(input())
chu=list(map(int,input().split(" ")))
chu.sort()

num = 1
for c in chu:
    if c <= num:
        num += c
    else:
        break
print(num)