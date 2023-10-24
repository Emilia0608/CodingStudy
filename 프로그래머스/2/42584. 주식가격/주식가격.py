def solution(prices):
    not_blue={}
    for i in range(0, len(prices)):
        not_blue[i]=0 # 시작시 기본값 1세팅 
        for j in range(i+1, len(prices)):
            if prices[i]>prices[j]:
                not_blue[i]=not_blue.get(i)+1
                break
            else:
                not_blue[i]=not_blue.get(i)+1
    answer=list(not_blue.values())
    return answer