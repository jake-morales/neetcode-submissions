from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = {}

        # -4 -1 -1 0 1 2 
        #    -1 -1     2
        for i in range(len(nums)-2):
            # 0 = nums[i] + nums[j] + nums[k]
            # nums[j] + nums[k] = -nums[i]
            target = -nums[i]
            j = i+1
            k = len(nums)-1
            while (j < k):
                # print("Checks at ", i, ": ", nums[i], nums[j], nums[k])
                pair_sum = nums[j] + nums[k]
                if pair_sum == target:
                    # store triplet as tuple in hash
                    # This avoids duplicates because
                    # tuple is already sorted because i < j < k always
                    triplets[(nums[i],nums[j],nums[k])] = True
                    j += 1 # Keep searching
                elif pair_sum < target: # increase the sum
                    j += 1
                else: # j + k > target # reduce the sum
                    k -= 1
            
        return list(triplets.keys())



