class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        # nums [1 2 3 4 5]
        # pref [1* 1 2 6 24]
        # suff [120 60 20 5 1*]
        pref = [1] * length
        suff = [1] * length

        # Calculate prefix product arrays
        for i in range(1, length):
            pref[i] = nums[i - 1] * pref[i - 1]
        
        # Calculate suffix product arrays
        for i in range(length-2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]

        # print(pref)
        # print(suff)

        res = [0] * length
        for i in range(length):
            res[i] = pref[i] * suff[i]
        
        return res
            


# Calculating a max product, and dividing

# max_product = 1
# first_zero_idx = -1
# for i, num in enumerate(nums):
#     if num == 0:
#         if first_zero_idx == -1:
#             first_zero_idx = i
#         else: # Short circuit. More than 1 zero means output is all zeros.
#             return [0] * len(nums)
#     else:
#         max_product *= num

# if first_zero_idx != -1:
#     # Short circuit. A zero was found. Output is max product at
#     # the index and zeros elsewhere
#     ret = [0] * len(nums)
#     ret[first_zero_idx] = max_product
#     return ret


# res = [0] * len(nums)
# for i, num in enumerate(nums):
#     res[i] = max_product // num

# return res
