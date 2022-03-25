import sys
import heapq as h


heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    if m:
        # heapq 자체가 최소 힙이므로 m이 0이 아니면 heap에 m을 heappush했다.
        # push가 pop보다 빈도가 더 높을 것으로 예상해 m != 0 인 경우를 먼저 동작시켰다.
        h.heappush(heap, m)
    else:
        # m이 0일때
        if heap:
            # heap에 값이 하나라도 있을 때 heappop
            print(h.heappop(heap))
        else:
            # heapq에서 빈 heap이 되면 indexError 발생하므로 heap에 값이 하나도 없을 경우 0을 프린트했다.
            print(0)        