N = int(input())

stack=[]
output = []

for _ in range(N):
    query=input()

    if query.split(" ")[0]=="push":
        stack.append(int(query.split(" ")[-1]))
    
    elif query=="pop":
        if len(stack)==0:
            output.append(-1)
        else:
            output.append(stack.pop())
    
    elif query=="size":
        output.append(len(stack))

    elif query=="empty":
        if len(stack)==0:
            output.append(1)
        else:
            output.append(0)
    
    elif query=="top":
        if len(stack)==0:
            output.append(-1)
        else:
            output.append(stack[-1])

print("\n".join([str(o) for o in output]))