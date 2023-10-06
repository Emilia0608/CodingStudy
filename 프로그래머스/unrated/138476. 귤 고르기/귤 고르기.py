from collections import Counter

def solution(k, tangerine):
    tang_count = Counter(tangerine)
    tang_count=sorted(tang_count.items(), key=lambda x: x[1], reverse=True)
    i=0
    cnt=0
    while k>0:    
        k=k-tang_count[i][1]
        i=i+1
        cnt=cnt+1
    answer = cnt
    return answer
