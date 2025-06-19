'''
1. 폰켓몬 딕셔너리 생성, count해서 value에 넣기
2. 2/N 만큼 key를 순차적으로 뽑아서 세기
'''

def solution(nums):
    N=len(nums)
    pon={} # 폰켓몬 딕셔너리

    for num in nums:
        if num not in pon:
            pon[num]=0
        pon[num]+=1
    
    if len(pon.keys())>N//2:
        answer=N//2
    else:
        answer=len(pon.keys())
    return int(answer)