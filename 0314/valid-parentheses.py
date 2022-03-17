# 강의

def is_valid_parenthesis(s):
    pair = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    opener = "({["
    stack = []

    for char in s:
        if char in opener:
            stack.append(char)
        else:
            # 아예 opener가 없는 s 이므로 false 반환
            if not stack:
                return False
            top = stack.pop()
            if pair[char] != top:
                return False

    return not stack
