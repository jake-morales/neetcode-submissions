import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Reverse the order so it's a maxheap
        for i in range(len(stones)):
            stones[i] = stones[i] * -1

        heapq.heapify(stones)
        while len(stones) > 1:
            top = heapq.heappop(stones)
            sec = heapq.heappop(stones)
            print("top: ", top, ", sec: ", sec)
            if top == sec:
                continue
            elif top < sec:
                heapq.heappush(stones, top - sec)
            else:
                heapq.heappush(stones, sec - top)
        
        # Check if none remain
        if not len(stones):
            return 0

        # return the final element, but as a positive
        return heapq.heappop(stones) * -1

        