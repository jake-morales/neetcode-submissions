from collections import defaultdict

# 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        # {1: 1, 2: 2, 3: 3}

        # Count frequencies
        for num in nums:
            freq[num] += 1

        # Create buckets
        buckets = []
        for _ in range(len(nums) + 1):
            buckets.append([])


        # Populate buckets
        for key,val in freq.items():
            buckets[val].append(key)
        
        # Get top k nums from buckets
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
            

        return res




