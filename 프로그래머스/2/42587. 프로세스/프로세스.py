def solution(priorities, location):
    queue=[i for i in range(len(priorities))]
    done=[]
    
    while len(queue)!=0:
        if priorities[0]!=max(priorities):
            queue.append(queue.pop(0))
            priorities.append(priorities.pop(0))
        else:
            done.append(queue.pop(0))
            priorities.pop(0)
            
    for idx, d in enumerate(done):
        if d==location:
            answer=idx
            break
    return answer+1