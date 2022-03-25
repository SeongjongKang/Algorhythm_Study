import sys
import heapq as h

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
  m = int(sys.stdin.readline())
  if m:
    # heapq 자체가 최소 힙이므로 -m을 넣어 최대 힙으로 작동할 수 있도록 했다.
    # push가 pop보다 빈도가 더 높을 것으로 예상해 m != 0 인 경우를 먼저 동작시켰다.
    h.heappush(heap,-m)
  else:
    # m이 0일때
    if heap:
        #음수 값을 힙에 넣어주었으므로 반환 시 양수로 반환했다.
        print(-1*h.heappop(heap))
    else:
        # heapq에서 빈 heap이 되면 indexError 발생하므로 heap에 값이 하나도 없을 경우 0을 프린트했다.
        print(0)    
