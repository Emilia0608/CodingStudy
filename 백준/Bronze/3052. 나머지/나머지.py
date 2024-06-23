remain_list=[]

for i in range(10):
    #n=int(a.split("\n")[i])
    n=int(input())
    remains=n%42
    if remains not in remain_list:
        remain_list.append(remains)
print(len(remain_list))