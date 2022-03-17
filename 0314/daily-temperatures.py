
class Solution:
    def dailyTemperatures(self, T):
        answer = [0] * len(T)
        stack = []

        # enumeration() 함수는 기본적으로 인덱스와 원소로 이루어진 tuple을 만들어준다.
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer

T = [11, 5, 6, 10, 9 ,13, 4, 6]

answer = [0] * len(T)
stack = []

# enumeration() 함수는 기본적으로 인덱스와 원소로 이루어진 tuple을 만들어준다. 이 경우 i는 인덱스, cur는 값을 가진다.
for i, cur in enumerate(T):
    while stack and cur > T[stack[-1]]:
        last = stack.pop()
        answer[last] = i - last
    stack.append(i)