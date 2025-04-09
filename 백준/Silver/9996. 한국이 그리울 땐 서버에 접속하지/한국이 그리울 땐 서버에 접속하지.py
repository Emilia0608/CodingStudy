N=int(input())
pattern=input()
prefix=pattern.split("*")[0]
postfix=pattern.split("*")[-1]

for _ in range(N):
    word=input()
    if len(word)<len(prefix)+len(postfix):
        print("NE")
    elif word[:len(prefix)]==prefix and word[-len(postfix):]==postfix:
        print("DA")
    else:
        print("NE")