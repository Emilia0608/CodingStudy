def solution(bridge_length, weight, truck_weights):
    answer = 0
    '''
    1. 다리 큐, 경과 시간 answer
    2. 대기 트럭 truck_weight의 갯수가 0이 될 때까지
    3. 다리 큐 경과 시간이 bridge_lenght보다 크면 pop
    3. 다리 큐 합, 새로운 트럭 1개 총 합이 weight보다 작고, 갯수가 bridge_length보다 작으면 다리 큐에 올리기
    4. 다리 큐에 트럭 올릴 때, 경과 시간도 같이 리스트 형태로 올리기
    5. 트럭의 경과시간이 bridge_length를 경과할 때 queue에서 pop
    '''
    
    queue=list()
    while len(truck_weights)!=0 or len(queue)!=0:
        answer+=1
        queue=[[a, b + 1] for a, b in queue]

        if len(queue)!=0 and queue[0][1]>=bridge_length:
            queue.pop(0)
        try:        
            if sum([que[0] for que in queue])+truck_weights[0]<=weight and len(queue)+1<=bridge_length:
                queue.append([truck_weights.pop(0), 0])    
        except:
            pass
        
    return answer