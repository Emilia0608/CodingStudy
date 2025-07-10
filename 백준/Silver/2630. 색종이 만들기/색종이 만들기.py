N=int(input())
matrix=[]
for _ in range(N):
    matrix.append(list(map(int, input().split(" "))))
    
def find_max_recursive(matrix, white, blue, size):
    size = len(matrix)

    if matrix==[[1]*size]*size:
        blue+=1
        return white, blue
    
    elif matrix==[[0]*size]*size:
        white+=1
        return white, blue

    else:
        size = size // 2
        white, blue = find_max_recursive([m[:size] for m in matrix[:size]], white, blue, size)
        white, blue = find_max_recursive([m[size:] for m in matrix[:size]], white, blue, size)
        white, blue = find_max_recursive([m[:size] for m in matrix[size:]], white, blue, size)
        white, blue = find_max_recursive([m[size:] for m in matrix[size:]], white, blue, size)
        return white, blue
    
white, blue=find_max_recursive(matrix, 0, 0, 8)
print(white)
print(blue)