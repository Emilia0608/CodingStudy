def solution(clothes):
    cody={}
    for cloth in clothes:
        if cloth[1] not in cody:
            cody[cloth[1]]=0
        cody[cloth[1]]+=1
    answer=1
    for val in list(cody.values()):
        answer*=(val+1)
    answer-=1
    return answer