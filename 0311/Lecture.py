import string


text = 'hello, this is sparta'

counter = {}

# 21번 연산
for char in text:
    if not char.isalpha():
        continue
    if char in counter:
        counter[char] += 1
    else:
        counter[char] = 1

print(counter)

# 26*21번 연산
# counter2 = {}
# for lo in string.ascii_lowercase:
#     for char in text:
#         if lo == char:
#             if lo in counter2:
#                 counter2[lo] += 1
#             else:
#                 counter2[lo] = 1

# print(counter2)

arr = {3, 5, 6, 1, 2, 4}
num = 9

def is_number_exist(num, arr):
    for el in arr:
        if num == el:
            return True
    return False

