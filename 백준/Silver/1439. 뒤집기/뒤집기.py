nums=input()
cnt_dict={"0":0, "1":0}

current=nums[0]
for num in nums[1:]:
    if current!=num:
        cnt_dict[current]+=1
        current=num
cnt_dict[current]+=1

if cnt_dict["0"]<=cnt_dict["1"]:
    print(cnt_dict["0"])
else:
    print(cnt_dict["1"])
