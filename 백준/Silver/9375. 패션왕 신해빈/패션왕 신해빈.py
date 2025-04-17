case=int(input())
for _ in range(case):
    n=int(input())
    answer=1 # 경우의 수를 곱할 것이기에 초깃값 1 설정

    clothes={}
    for i in range(n):
        cloth=input()
        if cloth.split(" ")[1] not in clothes: # 종류 처음일 때
            clothes[cloth.split(" ")[1]]=1
        else:
            clothes[cloth.split(" ")[1]]+=1

    for keys in clothes.keys():
        answer*=(clothes[keys]+1) # 안 입는 경우 +1
    print(answer-1) # 다 안 입는 경우 -1

    