import heapq
'''
1. scoville의 0인덱스가 K 이상이면 break, return answer
2. scoville의 갯수가 1인데 K 미만이면 break, return -1
'''

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0]<K and len(scoville)>1:
        heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        answer+=1
    
    if len(scoville)==1 and scoville[0]<K:
        answer=-1
        
    return answer