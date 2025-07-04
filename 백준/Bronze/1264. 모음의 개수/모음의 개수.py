while True:
    sent=input()
    if sent=="#":
        break
    answer=0
    for i in sent:
        if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            answer+=1
    print(answer)