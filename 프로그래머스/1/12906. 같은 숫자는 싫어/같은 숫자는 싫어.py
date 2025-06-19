def solution(arr):
    answer = []
    
    for ar in arr:
        if len(answer)==0:
            answer.append(ar)
        elif answer[-1]==ar:
            pass
        else:
            answer.append(ar)
    return answer