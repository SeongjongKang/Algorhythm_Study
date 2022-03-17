import collections

from collections import Counter

class Solution:
        def remove_duplicate_letters(s):
            counter, stack, seen = collections.Counter(s), [], set()
            for char in s:
                counter[char] -= 1
                if char in seen:
                    continue
                while stack and char < stack[-1] and counter[stack[-1]] > 0:
                    seen.remove(stack.pop())
                stack.append(char)
                seen.add(char)
            return ''.join(stack)



s = 'cbacdcbc'
counter, stack = collections.Counter(s), []

for char in s:
    counter[char] -= 1
    if char in stack:
        continue
    # stack에 값이 있고, char이 stack의 가장 마지막 보다 작고, stack에 담겨있는 마지막 값이 중복으로 남아있는 경우
    while stack and char < stack[-1] and counter[stack[-1]] > 0:
        stack.pop()
    stack.append(char)

a = ''.join(stack)

print(a)


