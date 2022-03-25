def solution(dirs):
    moving = {'U' : (-1, 0),'D' : (1, 0),'R' : (0, 1),'L' : (0, -1)}
    visited = []
    def VisitLength(x,y):
        global answer
        answer = 0
        for char in dirs:
            a = moving[char][0]
            b = moving[char][1]
            if x+a < -5 or x+a > 5 or y+b < -5 or y+b > 5:
                continue
            else:
                x,y = x+a, y+b
                if [(x,y),(x-a,y-b)] not in visited and [(x-a,y-b),(x,y)] not in visited:
                    visited.append([(x,y),(x-a,y-b)])
                    answer += 1
    VisitLength(0,0)
    return answer

dirs = "ULURRDLLU"

print(solution(dirs))