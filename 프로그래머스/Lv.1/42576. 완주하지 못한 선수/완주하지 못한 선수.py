from collections import Counter

def solution(participant, completion):
    p_cnt = Counter(participant)
    c_cnt = Counter(completion)
    sub_result=p_cnt-c_cnt
    answer=list(sub_result.keys())[0]
    return answer
