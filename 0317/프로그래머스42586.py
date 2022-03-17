def solution(progresses, speeds):
    count = []
    answer = []
    num = 1
    for i in range(len(progresses)):
        p = progresses[i]
        sp = speeds[i]
        c = 1
        while p + sp < 100:     
            c += 1
            sp = sp + speeds[i]
        count.append(c)

        if i > 0:
            if count[i] <= count[i-1]:
                count[i] = count[i-1]
                num += 1
                if i == len(progresses)-1:
                    answer.append(num)
            else:
                answer.append(num)
                num = 1
                if i == len(progresses)-1:
                    answer.append(num)
    return answer
