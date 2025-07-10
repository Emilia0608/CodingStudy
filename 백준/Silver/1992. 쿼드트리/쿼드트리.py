N=int(input())
matrix=[]
for _ in range(N):
    matrix.append([int(i) for i in input()])
    
def find_max_recursive(matrix, answer, size):
    size = len(matrix)

    if matrix==[[1]*size]*size:
        answer+="1"
        return answer
    
    elif matrix==[[0]*size]*size:
        answer+="0"
        return answer

    else:
        answer+="("
        size = size // 2
        answer=find_max_recursive([m[:size] for m in matrix[:size]], answer, size)
        answer=find_max_recursive([m[size:] for m in matrix[:size]], answer, size)
        answer=find_max_recursive([m[:size] for m in matrix[size:]], answer, size)
        answer=find_max_recursive([m[size:] for m in matrix[size:]], answer, size)
        answer+=")"
        return answer
    
answer=find_max_recursive(matrix, "", len(matrix))
print(answer)