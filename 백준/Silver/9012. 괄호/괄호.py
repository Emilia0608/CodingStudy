N = int(input())

output = []
for _ in range(N):
    stack=[]

    valids=input()
    bool=True

    for valid in valids:
        if valid=="(":
            stack.append("(")
        else:
            if len(stack)!=0:
                stack.pop()
            else:
                bool=False
                break
    
    if len(stack)!=0 or bool==False:
        output.append("NO")
    else:
        output.append("YES")

print("\n".join([o for o in output]))