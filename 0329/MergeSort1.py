
# 정렬한 두 배열 정렬 합
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
# 아쉽게도 시간초과 아마도 리스트를 만들고 삭제하는 과정에서 많은 시간이 소요 된 것일 거다.
def MergeSort(lst):
    nums = []
    for i in range(len(lst)):
        nums.append([lst[i]])
    while len(nums[0]) < len(lst):
        idx = 0
        while idx <= len(nums)-2:
            nums[idx] = merge(nums[idx], nums[idx+1])
            del nums[idx+1]
            idx += 1
    return nums[0]
