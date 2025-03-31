N=int(input())

word_list=[]
for _ in range(N):
    word_list.append(input())

answer=""
for i in range(len(word_list[0])):
    check_char=""
    check_status=True
    for j in range(N):
        if check_char=="":
            check_char=word_list[j][i]
        else:
            if check_char!=word_list[j][i]:
                check_status=False
                break
        
    if check_status==False:
        answer+="?"
    else:
        answer+=check_char
print(answer)