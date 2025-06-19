def solution(s):
    answer = True
    s_list=[]
    
    '''
    1. s_list에 괄호 업데이트, 
    2. 열린 괄호면 추가
    3. 닫힌 괄호면 최근 괄호 열린 괄호인지 체크하고 pop 해서 제거, 열린 괄호가 없으면 false
    4. s_list의 갯수가 0이면 true, 아니면 false
    '''
    
    for _ in s:
        if _=="(":
            s_list.append("(")
        elif _==")":
            if s_list[-1:]==["("]:
                s_list.pop()
            else:
                answer=False
                break
                
    if len(s_list)!=0:
        answer=False

    return answer