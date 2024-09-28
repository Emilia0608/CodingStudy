N=int(input())
original_score=[]
for _ in range(N):
    original_score.append(int(input()))
original_score.reverse()

cnt=0
max_score=0

for i in range(len(original_score)):
    if i ==0:
        max_score=original_score[i]
    else:
        if max_score<=original_score[i]:
            max_score=max_score-1
            cnt+=original_score[i]-max_score
        else:
            max_score=original_score[i]

print(cnt)