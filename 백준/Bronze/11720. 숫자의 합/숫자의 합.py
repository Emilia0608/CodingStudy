n=int(input())
s=input()

sum=0
for i in range(n):
    sum+= ord(s[i]) - ord('0')
print(sum)