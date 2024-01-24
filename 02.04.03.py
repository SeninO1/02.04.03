a = input()
a = a.replace(' ', '')
a = set(a)

for i in range(len(a)):
    b = input()
    if b in a:
        print('YES')
    else:
        print('NO')