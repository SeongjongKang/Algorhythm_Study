import string


def get_idx_naive(word):
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        char = word[i]
        for j in range(len(string.ascii_lowercase)):
            lo = string.ascii_lowercase[j]
            if result[j] == -1 and char == lo:
                result[j] = i
    print(' '.join([str(num) for num in result]))

# range(10)을 호출하면 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 가 들어있는 반복 가능한 객체 반환

def get_idx(word):
    # point 1. ord
    # point 2. O(n^2) -> O(n)
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        idx = ord(word[i]) - 97
        if result[idx] == -1:
            result[idx] = i
    print(' '.join([str(num) for num in result]))

# ord(): 문자를 아스키 코드로 변환
# chr(): 아스키 코드를 문자로 변환

get_idx_naive('baekjoon')
get_idx('baekjoon')