def solution(keymap, targets):
    tmp=''
    for word in targets:
        tmp+=word
    tmp_dict=dict.fromkeys(tmp)
    for c in tmp_dict.keys():
        tmp_list=[]
        for key in keymap:
            index=key.find(c)
            tmp_list.append(index)
        tmp_list=list(set(tmp_list))
        if len(tmp_list)==1 and tmp_list[0]==-1:
            tmp_dict[c]=-1
        else:
            if min(tmp_list)==-1:
                tmp_list.remove(-1)
                tmp_dict[c]=min(tmp_list)+1
            else:
                tmp_dict[c]=min(tmp_list)+1
    answer=[]
    for target in targets:
        result=0
        no_data=''
        for c in target:
            # -1 일 때 예외 처리 하나만 안되도 불가하기에
            if tmp_dict[c]==-1:
                result=-1
                no_data='error'
                answer.append(result)
                break
            else:
                result+=tmp_dict[c]
        if no_data!='error':
            answer.append(result)    
    return answer
