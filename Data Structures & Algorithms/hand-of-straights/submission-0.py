from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        h = Counter(hand)
        heap = []
        for i in h:
            heapq.heappush(heap, i)
        while heap:
            num = heap[0]
            for i in range(groupSize):
                if h[num+i] <=0:
                    return False
                h[num+i]-=1
                if h[num+i] == 0:
                    if heap[0] != num+i:
                        return False
                    heapq.heappop(heap)
        
        return True

        

        