# 인강 풀이
s=input()

check=[-1] * 26 #체크 배열

for i in range(len(s)):
    index=ord(s[i]) - ord('a') #아스키코드 변환

    if check[index]==-1:
        check[index]=i

for i in range(26):
    print(check[i], end=" ")