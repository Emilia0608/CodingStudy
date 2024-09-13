N, M= map(int, input().split())

first_list=list(map(int,input().split()))
second_list=list(map(int,input().split()))

n=0
m=0
answer=[]

while n < N and m < M:
  first_num=first_list[n]
  second_num=second_list[m]

  if first_num < second_num:
    answer.append(first_num)
    n+=1
  else:
    answer.append(second_num)
    m+=1

if n != N:
  answer.extend(first_list[n:])
elif m!=M:
  answer.extend(second_list[m:])

for a in answer:
  print(a)