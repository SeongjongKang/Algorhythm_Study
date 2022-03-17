
num = int(input())

for k in range(num):
    check = input()
    s = list(check)
    sum = 0

    for c in s:
        if c is '(':
            sum += 1
        elif c is ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break

    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')



