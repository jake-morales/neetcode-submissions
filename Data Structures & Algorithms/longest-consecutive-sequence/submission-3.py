from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = defaultdict(bool)
        for num in nums:
            hash[num] = True

        # print("hash: ", hash)

        max_length = 0
        for num in nums:
            # print("\n current num", num)
            if hash[num-1]: # Not start of sequence
                continue
            
            curr_length = 1
            # print("sequence: ")
            while hash[num+1]:
                # print(num, end=" ")
                curr_length += 1
                num += 1

            # print("\t curr length: ", curr_length)
            max_length = max(max_length, curr_length)
            # print("new max_length: ", max_length)
        
        return max_length