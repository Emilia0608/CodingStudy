import sys

while True:
    line = sys.stdin.readline().rstrip('\n')

    if not line:
        break

    lower_cnt=0
    upper_cnt=0
    number_cnt=0
    space_cnt=0

    for w in line:
        if w.islower():
            lower_cnt+=1
        elif w.isupper():
            upper_cnt+=1
        elif w.isdigit():
            number_cnt+=1
        elif w==" ":
            space_cnt+=1
    print(f"{lower_cnt} {upper_cnt} {number_cnt} {space_cnt}")