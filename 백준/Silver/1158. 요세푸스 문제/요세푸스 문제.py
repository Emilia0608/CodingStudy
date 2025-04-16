N, K= map(int, input().split(" "))
people=[]
for i in range(1, N+1):
    people.append(i)

answer_list=[]

while len(people)!=0:
    if len(answer_list)==0:
        search=K-1
    else:
        while search>=len(people):
            search-=len(people)
    
    answer_list.append(str(people.pop(search)))
    search+=(K-1)
print(f"<{', '.join(answer_list)}>")