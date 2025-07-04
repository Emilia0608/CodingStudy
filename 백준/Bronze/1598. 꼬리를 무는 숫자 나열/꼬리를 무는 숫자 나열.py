N, M=map(int, input().split(" "))

n_x=N//4
m_x=M//4
n_y=N%4-1
m_y=M%4-1

if n_y==-1:
    n_y=3
    n_x-=1
if m_y==-1:
    m_y=3
    m_x-=1

answer=abs(n_x-m_x)+abs(n_y-m_y)
print(answer)