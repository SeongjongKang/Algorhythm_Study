def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i in range(len(citations)):
        if citations[i] != 0 and citations[i] > answer:
            answer += 1
        if citations[i] <= answer:
            return answer
    return answer


[10,9,8,7,6,5,4,3,2,1]
[4,0,0,0]