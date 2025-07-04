N=int(input())
calls = list(map(int, input().split(" ")))

total_y=0
total_m=0
for call in calls:
    y_fee=(call//30+1)*10
    m_fee=(call//60+1)*15

    total_y+=y_fee
    total_m+=m_fee

if total_m<total_y:
    print(" ".join(["M", str(total_m)]))
elif total_m>total_y:
    print(" ".join(["Y", str(total_y)]))
else:
    print(" ".join(["Y", "M", str(total_y)]))