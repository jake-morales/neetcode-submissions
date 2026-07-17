class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            # Impossible to find triplet because
            # all numbers to right are also positive
            if nums[i] > 0:
                break

            # Skip duplicates. It's guaranteed to have
            # already found all related triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                # print("Checks at ", i, ": ", nums[i], nums[j], nums[k])
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum < 0:  # Increase the three_sum
                    j += 1
                elif three_sum > 0:  # Decrease the three_sum
                    k -= 1
                else:  # triplet found
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # skip duplicates for both pointers
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1

        return triplets
