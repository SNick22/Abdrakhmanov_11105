from collections import deque

a = input().split()
elems = deque()
oper = deque()

for item in a:
    if item not in ['-', '+', '*', '/', '(', ')']:
        elems.append(item)
    elif item in ['(', ')']:
        continue
    else:
        oper.appendleft(item)
result = str(elems + oper)

print(result)