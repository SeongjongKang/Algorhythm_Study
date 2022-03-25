import heapq

def test_maxheap_heapq(lst, k):
    # k개의 인자를 iterable인 lst안 에서 큰 순서로 뽑아 리스트로 만든다. 그 리스트의 마지막 값을 추출한다.
    return heapq.nlargest(k, lst)[-1]

def test_maxheap_heapq(lst, k):
    # lst를 역순으로 정렬(내림차순)한 후 k번째 index 즉 [k-1]의 값을 추출한다.
    return sorted(lst, reverse=True)[k-1]