N, X= map(int, input().split(" "))
nums=list(map(int, input().split(" ")))
answer= [str(i) for i in nums if i <X]
print(" ".join(answer))