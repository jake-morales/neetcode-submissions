from collections import defaultdict

class Solution:
    # [3 4 2 1 5 5 2]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1

        # Create n buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # Fill in buckets
        for num,count in freq.items():
            buckets[count].append(num)
        
        # Get the top k buckets
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res
        




