# 시간초과로 실패
def solution(progresses, speeds):
    count = []

    for i in range(len(progresses)):
        p = progresses[i]
        sp = speeds[i]
        c = 1
        while p + sp < 100:     
            c += 1
            sp = sp + speeds[i]
        count.append(c)
    
    for i in range(len(count)):
        while count[i] >= count[i+1]:
            count[i+1] = count[i]
    count = list(set(count))

    return count

