def solution(s):
    answer=""
    for char in s:
        if char==" " or type(char)==int:
            answer+=char
        else:
            if len(answer)==0 or answer[-1]==" ":
                answer+=char.upper()
            elif type(answer[-1])==int:
                answer+=char.lower()
            else:
                answer+=char.lower()
    return answer