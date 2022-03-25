def solution(numbers, target):
    # DFS 재귀 방식으로 
    answer = 0
    def dfs(idx, cur_sum):
        if idx == len(numbers):
            if cur_sum == target:
                nonlocal answer
                answer += 1
                return
            else:
                return
        sum_plus = cur_sum + numbers[idx]
        dfs(idx + 1, sum_plus)
        sum_minus = cur_sum - numbers[idx]
        dfs(idx + 1, sum_minus)
    dfs(0, 0)
    return answer