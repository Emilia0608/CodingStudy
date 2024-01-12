def solution(array, commands):
    answer = []
    for command in commands:
        i=command[0]
        j=command[1]
        k=command[2]
        tmp_list=array[i-1:j]
        tmp_list.sort()
        tmp=tmp_list[k-1]
        answer.append(tmp)
    return answer
