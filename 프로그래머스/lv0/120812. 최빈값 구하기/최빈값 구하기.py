import statistics

def solution(array):
    mode_num=statistics.multimode(array)
    if len(mode_num)>1:
        answer=-1
    else:
        answer=mode_num[0]
    return answer



