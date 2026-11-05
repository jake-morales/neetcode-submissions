# [-1,0,2,4,6,8]
#       ^


# target = 2
# [-1,0,2]
#   L
#       R
#     M
# [-1,0,2]
#       L
#       R  
#       M

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while (l <= r):
            # print("l: ", l, ", r: ", r)
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]: # Shift left
                r = mid - 1
            else: # shift right
                l = mid + 1

        return -1
