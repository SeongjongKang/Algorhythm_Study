# 교재

def is_valid_parenthesis(s):
    pair = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    stack = []

    for char in s:
        # char가 closer가 아닌 opener인 경우
        if char not in pair:
            # stack에 append
            stack.append(char)

        # stack이 비어있지 않고(비어있으면 opener가 없는 closer쌍이 존재하는 것이므로), closer의 쌍이 stack에서 pop()한 가장 top이랑 다르면
        elif not stack or pair[char] != stack.pop():
            return False

    #stack에 값이 남아있다면 closer든 opener든 쌍이 맞지 않다는 뜻이므로, stack에 아무 값도 없으면 True 반환
    return len(stack) == 0

