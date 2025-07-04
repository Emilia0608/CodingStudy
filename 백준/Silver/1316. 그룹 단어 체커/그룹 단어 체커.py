N=int(input())
answer=0

for _ in range(N):
    word=input()
    past=[]
    check=""
    status=True

    for w in word:
        if check=="" or check==w:
            check=w
        elif check!=w and w not in past:
            past.append(check)
            check=w
        else:
            status=False
            break
    if status==True:
        answer+=1

print(answer)