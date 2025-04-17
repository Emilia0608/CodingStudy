import sys

left_stack = list(sys.stdin.readline().rstrip())
right_stack = []

M = int(sys.stdin.readline())

for _ in range(M):
    command = sys.stdin.readline().rstrip()
    
    if command == "L":
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command == "D":
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command == "B":
        if left_stack:
            left_stack.pop()
    elif command.startswith("P "):
        _, char = command.split()
        left_stack.append(char)

print(''.join(left_stack + right_stack[::-1]))  