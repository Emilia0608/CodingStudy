N=int(input())
for i in range(1, 2*N):
    star=""
    if i<=N: # 윗부분
        star+="*"*i # 별
        star+=" "*2*(N-i) # 공백
        star+="*"*i # 별
    else: # 아랫부분
        star+="*"*(2*N-i) 
        star+=" "*2*(i-N) 
        star+="*"*(2*N-i)
    print(star)