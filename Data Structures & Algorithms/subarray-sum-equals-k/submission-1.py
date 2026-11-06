# nums = [2,-1,1,2], k = 2

# prefix = [2,-1,1,2]

# It's similar to 2 sum. You use a hash to count how many targets have already passed. except this time the target is a particular prefix sum that exists.

# prefix sum let's you quickly calculate the sum of the subarray between L and R. The sum between L and R is prefix[R] - prefix[L-1]. So, if we want to know which target is needed to get a sum of k, then we need to find all prefix sums ("J-1"'s) where it equals prefix[i] - k.


from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # total count of subarrays that add up to k
        num_subarrays = 0
        # prefix[i] basically
        curr_sum = 0

        # Keeping track of which prefix sums exist previously
        prefix_counts = defaultdict(int)
        # Helps with the math. since [2] is a valid subarray, we need a prefix[j-1] that doesn't exist. so we artificially set prefix of 0 to 1.
        # From the solution: "The hash map must start with {0: 1} to handle subarrays that start from index 0. Without this initialization, subarrays where prefixSum == k from the beginning will not be counted."
        prefix_counts[0] = 1

        # Iterate for each num
        for num in nums:
            # Get prefix[i]
            curr_sum += num
            # Calculate the target
            target = curr_sum - k
            # add the valid prefix[J-1]'s to the total
            num_subarrays += prefix_counts[target]
            # Increment the count of this prefix to the counts
            prefix_counts[curr_sum] += 1

        # Return the total
        return num_subarrays