import sys
import heapq
heap = []
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, n)
