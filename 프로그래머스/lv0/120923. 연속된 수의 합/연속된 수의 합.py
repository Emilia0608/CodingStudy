def solution(num, total):
    answer = []
    
    # 등차수열 합
    # Sn=2an+n^2-n/2
    a=total/num+0.5-0.5*num
    for i in range (0, num):
        answer_num=a+i
        answer.append(answer_num)
    return answer
    