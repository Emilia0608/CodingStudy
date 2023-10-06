import re
def solution(new_id):
    # answer=''
    
    # 1단계 대문자 -> 소문자
    answer=new_id.lower()
    
    # 2단계  '!', '@', '#', '*' 문자 제거
    answer=re.sub('[^a-z0-9-_.]','',answer)
    
    # 3단계 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    answer=re.sub(r'\.{2,}', '.', answer)
    
    # 4단계 아이디의 처음에 위치한 '.' 제거
    answer=answer.lstrip('.')
    answer=answer.rstrip('.')
    
    # 5단계 빈 문자열 -> a 대입
    if len(answer)==0:
        answer="a"
        
    # 6단계 16자 이상 -> 첫 15개 문자만 사용
    
    if len(answer)>15:
        answer=answer[:15]
        answer=answer.rstrip('.')
        
    # 7단계 2글자 이하 -> 길이가 3 될때까지 마지막 문자 붙히기
    if len(answer)<3:
        answer=answer+answer[-1]*(3-len(answer))
            
    return answer
