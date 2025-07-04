def solution(numbers, target):
    current_sum=[]
    current_sum.append(numbers[0])
    current_sum.append(-numbers[0])

    current_tmp=[]
    current_idx=1

    while current_idx!=len(numbers):
        for num in current_sum:
            current_tmp.append(num+numbers[current_idx])
            current_tmp.append(num-numbers[current_idx])
        current_sum=current_tmp
        current_tmp=[]
        current_idx+=1

    answer=0
    for sum in current_sum:
        if sum==target:
            answer+=1       
        
    return answer