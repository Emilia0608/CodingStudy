import sys

while True:
    line = list(map(int, sys.stdin.readline().split()))

    if line== [0, 0]:
        break

    else:
        w, h = line
        
        info = []
        for _ in range(h):
            info.append(list(map(int, sys.stdin.readline().split())))

        rows, cols = h, w
        visited=[[False]* cols for _ in range(rows)]

        def dfs(i, j, info, visited):
            directions=[(-1,0), (1,0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

            stack=[(i,j)]
            visited[i][j]=True

            while stack:
                x, y = stack.pop()

                for dx, dy, in directions:
                    nx, ny = x+dx, y+dy

                    if 0 <= nx < len(info) and 0<=ny< len(info[0]):
                        if info[nx][ny]==1 and not visited[nx][ny]:
                            visited[nx][ny]=True
                            stack.append((nx, ny))

        count=0

        for i in range(rows):
            for j in range(cols):
                if info[i][j]==1 and not visited[i][j]:
                    dfs(i, j, info, visited)
                    count+=1
        print(count)