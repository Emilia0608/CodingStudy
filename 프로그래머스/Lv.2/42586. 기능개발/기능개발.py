import math

def solution(progresses, speeds):
    left_progresses=[]
    return_list=[]
    update_day=0

    for i, p in enumerate(progresses):
        left_progresses.append(math.ceil((100-p)/speeds[i]))

    for i in range(len(left_progresses)):
        if i==0:
            update_day=left_progresses[i]
            return_list.append(1)
        else:
            if left_progresses[i]<=update_day:
                return_list[-1]=return_list[-1]+1
            else:
                return_list.append(1)
                update_day=left_progresses[i]
            
    return return_list

# progresses=[93, 30, 55]
# speeds=	[1, 30, 5]
# left_progresses=[]
# return_list=[]
# update_day=0

# for i, p in enumerate(progresses):
#     left_progresses.append(math.ceil((100-p)/speeds[i]))
    
# for i in range(len(left_progresses)):
#     if i==0:
#         update_day=left_progresses[i]
#         return_list.append(1)
#     else:
#         if left_progresses[i]<=update_day:
#             return_list[-1]=return_list[-1]+1
#         else:
#             return_list.append(1)
#             update_day=left_progresses[i]
            
# print(return_list)




