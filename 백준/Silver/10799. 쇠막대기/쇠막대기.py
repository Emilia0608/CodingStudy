pipe=input()

candidate=[]
total=0


for i in range(len(pipe)):
    if pipe[i] == "(":
        candidate.append(i)
    else:
        candidate.pop()
        if pipe[i-1]=="(": # 레이저
            total+=len(candidate)
        else: # 쇠막대기
            total+=1

print(total)