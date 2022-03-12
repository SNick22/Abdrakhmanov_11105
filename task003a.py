a = input().split()
i = 0
while i < len(a):
    if a[i] == '+' or a[i] == '-' or a[i] == '*' or a[i] == '/':
        if i+1 != len(a) and (a[i+1] == '+' or a[i+1] == '-' or a[i+1] == '*' or a[i+1] == '/'):
            a[i-2] = '(' + a[i-2] + a[i] + a[i-1] + ')'
            a.pop(i)
            a.pop(i-1)
            i -= 1
        else:
            a[i-2] = a[i-2] + a[i] + a[i-1]
            a.pop(i)
            a.pop(i - 1)
            i -= 1
    else:
        i += 1
print(a.pop())