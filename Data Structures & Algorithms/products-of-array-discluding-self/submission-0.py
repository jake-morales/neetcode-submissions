class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max_product = 1
        first_zero_idx = -1
        for i, num in enumerate(nums):
            if num == 0:
                if first_zero_idx == -1:
                    first_zero_idx = i
                else: # Short circuit. More than 1 zero means output is all zeros.
                    return [0] * len(nums) 
            else:
                max_product *= num

        if first_zero_idx != -1:
            # Short circuit. A zero was found. Output is max product at 
            # the index and zeros elsewhere
            ret = [0] * len(nums)
            ret[first_zero_idx] = max_product
            return ret


        res = [0] * len(nums)
        for i, num in enumerate(nums):
            res[i] = max_product // num
        
        return res