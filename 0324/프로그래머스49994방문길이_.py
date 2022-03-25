# Dict을 이용하여 UDRL방향을 나타내는 변수들을 깔끔하게 정리 할 수 있다.
def solution(dirs):
    visited = []
    def VisitLength(x,y):
        global answer
        answer = 0
        for char in dirs:
            if char is 'U':
                if x == 0:
                    continue
                a,b=x,y
                x,y=x-1,y
            if char is 'D':
                if x == 10:
                    continue
                a,b=x,y
                x,y=x+1,y
            if char is 'R':
                if y == 10:
                    continue
                a,b=x,y
                x,y=x,y+1
            if char is 'L':
                if y == 0:
                    continue
                a,b=x,y
                x,y=x,y-1
            if [(a,b),(x,y)] not in visited and [(x,y),(a,b)] not in visited:
                visited.append([(a,b),(x,y)])
                answer += 1
    VisitLength(5,5)
    return answer

