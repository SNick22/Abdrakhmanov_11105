a = input().split()
i = 0
while i < len(a):
    if a[i] == '+' or a[i] == '-' or a[i] == '*' or a[i] == '/':
        a[i-2] = '(' + a[i-2] + a[i] + a[i-1] + ')'
        a.pop(i)
        a.pop(i-1)
        i -= 1
    else:
        i += 1
print(a.pop())