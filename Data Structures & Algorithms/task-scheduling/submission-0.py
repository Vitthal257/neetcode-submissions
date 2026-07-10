from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        map = Counter(tasks)
        heap = [-c for c in map.values()]
        time = 0
        q = deque()
        heapq.heapify(heap)

        while heap or q:
            time += 1
    
            if heap:
                freq = heapq.heappop(heap)
                freq += 1  # increment (remember it's negative!)
                if freq != 0:  # still has remaining count
                    q.append((freq, time + n))  # available after cooldown
    
            if q and q[0][1] <= time:  # is front of queue ready?
                heapq.heappush(heap, q.popleft()[0])

        return time
