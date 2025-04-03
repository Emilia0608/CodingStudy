N=int(input())

rain_info=[]
for _ in range(N):
    rain_info.append(list(map(int,input().split())))

def dfs(r, c, rain_status, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    stack = [(r, c)]  
    visited[r][c] = True
    
    while stack:
        x, y = stack.pop()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < len(rain_status) and 0 <= ny < len(rain_status[0]):
                if rain_status[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

def count_zero_groups(rain_status):
    if not rain_status:
        return 0
    
    rows, cols = len(rain_status), len(rain_status[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            if rain_status[i][j] == 1 and not visited[i][j]:
                dfs(i, j, rain_status, visited)
                count += 1 
    
    return count

rain_height=[]
rain_height.append(0)  
for info in rain_info:
    rain_height.extend(info)
rain_height=list(set(rain_height))


rain_status_dict={}

for height in rain_height:
    rain_status_dict[height]=[]
    for row in rain_info:
        tmp=[]
        for value in row:
            if value<=height:
                tmp.append(0) # 잠김
            else:
                tmp.append(1) # 안잠김
        rain_status_dict[height].append(tmp)

count_list=[]
for key in rain_status_dict.keys():
    rain_status=rain_status_dict[key]
    count=count_zero_groups(rain_status)
    count_list.append(count)

print(max(count_list))
