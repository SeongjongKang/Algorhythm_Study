# 재귀를 이용하여 구현
def mergesort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    L = lst[:mid] # 인덱스 0~mid-1까지
    R = lst[mid:] # 인덱스 mid ~ len(lst)-1 까지
    return merge(mergesort(L), mergesort(R))

def merge(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result
