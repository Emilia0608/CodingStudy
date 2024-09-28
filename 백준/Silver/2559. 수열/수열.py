# 인강 풀이
N, K=list(map(int,input().split()))
A=list(map(int,input().split()))

psum= [0] * N
psum[0] = A[0]

# 누적합 psum 만들기
for i in range(1, N):
    psum[i] = psum[i-1] + A[i]

# 연속된 K일 온도 합
temp_sum =[]
for i in range(0, N-K+1):
    # i ~ i + K -1
    if i==0:
        sum = psum[i+K-1]
    else:
        sum= psum[i+K-1]-psum[i-1] 
    temp_sum.append(sum)

print(max(temp_sum))