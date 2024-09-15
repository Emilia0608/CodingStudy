T=int(input())
for _ in range(T):
    N, M= map(int, input().split())
    A=list(map(int, input().split()))
    B=list(map(int, input().split()))
    A.sort()
    B.sort()

    start =0
    end =0
    cnt =0

    while start<N:
        if end == M:
            cnt += end
            start += 1
        else:
            if A[start]>B[end]:
                end +=1
            else:
                start +=1
                cnt += end
            

    print(cnt)
