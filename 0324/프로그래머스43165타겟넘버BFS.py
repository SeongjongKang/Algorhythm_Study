from collections import deque
# BFS 즉 Queue를 이용하여 트리의 root부터 height를 증가시키며 sum 값을 더해 나갔다.
def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)]) 
    while queue:
        sum, height = queue.popleft()
        if height > len(numbers):
            break
        elif height == len(numbers) and sum == target:
            answer += 1
        queue.append((sum+numbers[height-1], height+1))
        queue.append((sum-numbers[height-1], height+1))

    return answer