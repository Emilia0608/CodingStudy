N=int(input())
nums=list(map(int, input().split(" ")))

exists=[i+1 for i in range(N)]
answer_list=[]
search_index=0

while len(exists)>0:
    if search_index>=len(exists):
        search_index-=len(exists)
    while search_index<0:
        search_index+=len(exists)
    balloon_val=nums[search_index]
    nums.pop(search_index)
    answer_list.append(str(exists.pop(search_index)))
    
    if not exists:
        break

    if balloon_val<0:
        search_index+=(balloon_val)
    else:
        search_index+=(balloon_val-1)

    search_index %= len(exists)
print(" ".join(answer_list))