# nums: 2 3 1 5 4
# k = 2
#       ^
#         ^
#           ^
#             ^
#               ^

# min heap: [5 4]
# Kicks out smallest number

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heapq.heappop(heap)