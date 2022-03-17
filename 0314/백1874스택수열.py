n = int(input())
stack=[]
answer=[]
sum = 1
temp = True

for i in range(n):
    x = int(input())

    while x >= sum:
        stack.append(sum)
        answer.append('+')
        sum += 1

    if x == stack[-1]:
        answer.append('-')
        stack.pop()
    else:
        temp = False
if temp is False:
    print('NO')
else:
    for i in answer:
        print("\n".join(i))

